#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
OUTIL INTERNE #03 : MEDIA QUALITY AUDITOR — CANAL 1 (VARIANTE 1 : MCP CLASSIC STDIO)
========================================================================================
Serveur MCP JSON-RPC 2.0 exposant :
1. audit_media_folder
2. get_certified_hero_candidates
3. clean_duplicate_media
4. run_quality_and_tests_suite
========================================================================================
"""

import sys
import os
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional

current_dir = Path(__file__).resolve().parent
tool_root = current_dir.parent.parent
if str(tool_root) not in sys.path:
    sys.path.insert(0, str(tool_root))

from canal_sdk_cli.sdk import MediaAuditorPipeline

PIPELINE = MediaAuditorPipeline()
WORKSPACE_ROOT = tool_root.parent.parent.resolve()
TEST_RUNNER = tool_root / "tests" / "run_all_suites.py"

TOOLS_SCHEMA = [
    {
        "name": "audit_media_library",
        "description": "Audite l'ensemble de la bibliothèque multimédia (frontend/public/images/) : dénombre les fichiers par sous-dossier, calcule la taille totale et détecte les doublons par empreinte MD5.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "base_dir": {"type": "string", "description": "Répertoire optionnel à auditer (défaut frontend/public/images)."}
            },
            "required": []
        }
    },
    {
        "name": "audit_media_folder",
        "description": "Analyse un dossier d'images (Pillow + MD5) : résolutions, formats, poids et qualification VALID_HD, REJECTED_LOW_RES ou DUPLICATE.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "folder_path": {"type": "string", "default": "frontend/public/assets/catalogue_verre"},
                "min_width": {"type": "integer", "default": 1200},
                "min_height": {"type": "integer", "default": 700}
            },
            "required": []
        }
    },
    {
        "name": "get_certified_hero_candidates",
        "description": "Extrait la liste des images certifiées HD répondant aux exigences de netteté.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "folder_path": {"type": "string", "default": "frontend/public/assets/catalogue_verre"}
            },
            "required": []
        }
    },
    {
        "name": "clean_duplicate_media",
        "description": "Détecte et purge les fichiers en doublon (empreintes MD5 identiques ou suffixes ' copy').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "folder_path": {"type": "string", "default": "frontend/public/assets/catalogue_verre"},
                "dry_run": {"type": "boolean", "default": True}
            },
            "required": []
        }
    },
    {
        "name": "run_quality_and_tests_suite",
        "description": "Exécute les 4 couches de tests de 03_media_quality_auditor (Unitaires, Intégration, Validation/Performance, Smoke).",
        "inputSchema": {"type": "object", "properties": {}, "required": []}
    }
]


def audit_full_media_library(base_dir: Optional[str] = None) -> Dict[str, Any]:
    images_root = Path(base_dir) if base_dir else WORKSPACE_ROOT / "frontend" / "public" / "images"
    if not images_root.exists():
        return {"error": f"Dossier {images_root} introuvable."}

    import hashlib
    categories: Dict[str, Dict[str, Any]] = {}
    hash_to_files: Dict[str, List[str]] = {}
    total_files = 0
    total_bytes = 0

    for root, dirs, files in os.walk(images_root):
        rel_cat = Path(root).relative_to(images_root).as_posix()
        cat_name = rel_cat.split("/")[0] if rel_cat != "." else "root"
        if cat_name not in categories:
            categories[cat_name] = {"count": 0, "size_kb": 0.0}

        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".avif", ".svg")):
                fp = Path(root) / file
                st = fp.stat()
                total_files += 1
                total_bytes += st.st_size
                categories[cat_name]["count"] += 1
                categories[cat_name]["size_kb"] = round(categories[cat_name]["size_kb"] + (st.st_size / 1024), 1)

                try:
                    h = hashlib.md5(fp.read_bytes()).hexdigest()
                    rel_p = fp.relative_to(WORKSPACE_ROOT).as_posix()
                    if h not in hash_to_files:
                        hash_to_files[h] = []
                    hash_to_files[h].append(rel_p)
                except Exception:
                    pass

    duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}

    return {
        "status": "PASS" if len(duplicates) == 0 else "INFO",
        "total_images": total_files,
        "total_size_mb": round(total_bytes / (1024 * 1024), 2),
        "categories": categories,
        "duplicates_count": len(duplicates),
        "duplicates": duplicates
    }


def resolve_path(p: str) -> str:
    if os.path.isabs(p):
        return p
    candidate = WORKSPACE_ROOT / p
    if candidate.exists():
        return str(candidate)
    fallback = WORKSPACE_ROOT / "frontend" / "public" / "assets" / "catalogue_verre"
    return str(fallback)


def handle_request(req: Dict[str, Any]) -> Dict[str, Any]:
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "03-media-quality-auditor-mcp",
                    "version": "2.0.0"
                }
            }
        }

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS_SCHEMA}}

    if method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        folder_path = resolve_path(args.get("folder_path", "frontend/public/assets/catalogue_verre"))

        try:
            if tool_name == "audit_media_library":
                base_dir = args.get("base_dir")
                result = audit_full_media_library(base_dir)
            elif tool_name == "audit_media_folder":
                min_w = int(args.get("min_width", 1200))
                min_h = int(args.get("min_height", 700))
                result = PIPELINE.audit_directory(folder_path, min_width=min_w, min_height=min_h)
            elif tool_name == "get_certified_hero_candidates":
                result = PIPELINE.get_certified_hero_candidates(folder_path)
            elif tool_name == "clean_duplicate_media":
                dry_run = bool(args.get("dry_run", True))
                result = PIPELINE.clean_duplicates(folder_path, dry_run=dry_run)
            elif tool_name == "run_quality_and_tests_suite":
                proc = subprocess.run([sys.executable, str(TEST_RUNNER), "--json"], capture_output=True, text=True, check=False)
                result = json.loads(proc.stdout)
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Outil inconnu : {tool_name}"}
                }

            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2, ensure_ascii=False)}]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "isError": True,
                    "content": [{"type": "text", "text": f"Erreur d'exécution : {str(e)}"}]
                }
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Méthode non implémentée : {method}"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            if res:
                sys.stdout.write(json.dumps(res, ensure_ascii=False) + "\n")
                sys.stdout.flush()
        except Exception as err:
            sys.stdout.write(json.dumps({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(err)}
            }) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()

# mcp-03-media-quality-auditor

[![Pôle Stratégique](https://img.shields.io/badge/P%C3%B4le-02_POLE_ECOMMERCE_CATALOGUE-blue.svg)](#)
[![Nature](https://img.shields.io/badge/Nature-OUTIL-orange.svg)](#)
[![Visibilité](https://img.shields.io/badge/Visibilit%C3%A9-CODE-green.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-purple.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-V14.1%20Clean%20Architecture-teal.svg)](#)

> **OUTIL OPEN-SOURCE (Marketing Image & E-commerce)**  
> Contrôleur qualité qui analyse la netteté, la résolution et élimine les doublons d'images par calcul de hash perceptuel.

---

## 1. Carte d'Identité & Rôle Métier

| Champ Stratégique | Valeur Officielle |
| :--- | :--- |
| **Composant Officiel** | `mcp-03-media-quality-auditor` |
| **Pôle d'Appartenance** | **Pôle 2 : La Suite E-commerce & Ingestion de Catalogues Marchands** |
| **Modèle Business** | **OUTIL OPEN-SOURCE (Marketing Image & E-commerce)** |
| **Politique de Visibilité** | **CODE PUBLIC OPEN-SOURCE (MIT)** |
| **Mission Principale** | Contrôleur qualité qui analyse la netteté, la résolution et élimine les doublons d'images par calcul de hash perceptuel. |
| **Architecture** | Clean Architecture Tri-Canal (STDIO / CLI / SDK In-Process) |

---

## 2. Guide d'Installation 1-Clic

### Option A : Installation Automatisée 1-Clic (Recommandée)
Exécutez simplement le script `install.py` à la racine du dépôt :

```bash
python install.py
```

Ce script effectue automatiquement :
1. La vérification de votre environnement Python (>= 3.10).
2. L'installation des dépendances requises en mode éditable (`pip install -e .` ou `npm install`).
3. La détection et l'injection automatique du serveur dans la configuration de Cursor (`%USERPROFILE%/.cursor/mcp.json`) sans écraser vos autres outils.

### Option B : Installation Manuelle Développeur
```bash
pip install -e .
```

---

## 3. Configuration Manuelle (Cursor, Antigravity, Claude Desktop)

Si vous préférez déclarer manuellement ce serveur dans votre fichier `.cursor/mcp.json` ou `mcp_config.json`, ajoutez le bloc suivant :

```json
{
  "mcpServers": {
    "mcp-03-media-quality-auditor": {
      "command": "python",
      "args": ["canal_mcp/mcp_classic_stdio/mcp_server.py"],
      "env": { "PYTHONIOENCODING": "utf-8" },
      "type": "stdio"
    }
  }
}
```

---

## 4. Catalogue Sémantique des Outils (`tools`)

Ce composant expose des outils déterministes prêts à être invoqués par un modèle de langage (LLM) :

| Nom de l'Outil (`tool`) | Rôle & Fonction Technique | Déclencheur d'Action (*Quand l'IA DOIT-ELLE l'appeler ?*) | Paramètres Requis | Sortie Retournée |
| :--- | :--- | :--- | :--- | :--- |
| `mcp_audit_image_resolution` | Vérifie les dimensions minimales, la netteté et le ratio des visuels de fiches produits. | **Avant la mise en ligne d'un catalogue de produits marchands.** | `image_path (str, requis), min_width (int, optionnel), min_height (int, optionnel)` | Rapport de conformité visuelle (résolution, format, flou éventuel). |
| `mcp_detect_duplicate_images` | Calcule le hash perceptuel (pHash/dHash) de milliers d'images pour regrouper les doublons. | **Dès qu'un dossier d'assets contient des images similaires avec des noms différents.** | `images_dir (str, requis), threshold (int, optionnel)` | Groupes d'images identiques ou quasi-identiques à nettoyer. |

---

## 5. Exemples Concrets de Prompts Utilisateur

Voici 3 exemples réels de requêtes que vous pouvez poser directement dans le chat de Cursor ou Claude Code pour faire travailler cet outil :

1. *« Scanne le dossier d'images produits et signale celles qui font moins de 800x800 pixels. »*
2. *« Détecte les doublons d'images par calcul de hash perceptuel dans le dossier public/images. »*
3. *« Génère un rapport de qualité des médias pour le catalogue e-commerce. »*

---

## 🛡️ Propriété Intellectuelle & Sécurité
- **Éditeur :** SNORBIK AI © 2026.
- **Classification :** Conforme à la Directive Maîtresse V14.1 (Recettes d'architecture sanctuarisées dans le Pôle 06).
- **Zéro Régression :** Respect strict des budgets de lignes et des normes de sécurité.

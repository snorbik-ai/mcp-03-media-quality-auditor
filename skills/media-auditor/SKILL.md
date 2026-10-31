---
name: mcp-03-media-auditor
description: Serveur MCP Media Quality Auditor : Audit de résolution, netteté et dédoublonnage par hash perceptuel.
---

# 🧬 SKILL ADN : MCP-03-MEDIA-AUDITOR
> **Classification :** Noyau Opérationnel Standardisé Snorbik AI (Directive Master V2.0)  
> **Mission :** Serveur MCP Media Quality Auditor : Audit de résolution, netteté et dédoublonnage par hash perceptuel.

---

## 1. Identité & Mission Critique

- **Nom officiel du Skill :** `mcp-03-media-auditor`
- **Rôle Fonctionnel :** Ce skill encapsule l'ADN technique, les règles de décision et les invariants opérationnels pour le sous-système `mcp-03-media-auditor`.
- **Déclencheur d'Activation :** Ce skill est activé dès qu'une IA ou un développeur intervient sur le périmètre correspondant ou traite des tâches de cette compétence.

---

## 2. Invariants Absolus & Interdictions (Vaccins)

Les règles suivantes sont formellement obligatoires et ne souffrent aucune dérogation :

- **INV-01 :** Seuil minimal de résolution pour fiches produits e-commerce : 800x800 px.
- **INV-02 :** Dédoublonnage infaillible via calcul de hash perceptuel pHash / dHash.
- **INV-03 :** Génération de rapports d'anomalies visuelles sans altérer les sources.

---

## 3. Protocole d'Exécution Pas-à-Pas

Pour accomplir les missions de ce skill avec 100% de réussite :

1. Scanner le répertoire d'images cibles.
2. Calculer les métriques de netteté et résolutions.
3. Détecter et regrouper les doublons via mcp_detect_duplicate_images.

---

## 4. Cartographie des Outils MCP & Scripts

Ce skill pilote et s'appuie sur les outils d'ingénierie suivants :

- `mcp_audit_image_resolution`
- `mcp_detect_duplicate_images`

---

## 5. Résilience, Erreurs Fréquentes & Fallback

- En cas d'image corrompue, l'isoler dans le dossier quarantine/ sans stopper le scan.

---

## 6. Procédure de Mutation (Enrichissement de l'ADN)

Ajustement des seuils de distance de Hamming selon le type d'asset (photo vs schéma technique).

---
*Scellé et certifié conforme par la Gouvernance Génomique Snorbik AI © 2026.*

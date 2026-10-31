# mcp-03-media-quality-auditor

[![Pôle Stratégique](https://img.shields.io/badge/P%C3%B4le-02_POLE_ECOMMERCE_CATALOGUE-blue.svg)](#)
[![Nature Commerciale](https://img.shields.io/badge/Nature-OUTIL-orange.svg)](#)
[![Visibilité](https://img.shields.io/badge/Visibilit%C3%A9-CODE-green.svg)](#)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Architecture%20Ports%20%26%20Adapters-teal.svg)](#)
[![Budget Lignes](https://img.shields.io/badge/R%C3%A8gle%20%235-%3C%20350%20Lignes%20Garanti-blueviolet.svg)](#)

> **OUTIL OPEN-SOURCE (Marketing Image & E-commerce)**  
> Génération de leads e-commerce sur LinkedIn. Détecte le flou, calcule le hash perceptuel et élimine les doublons d'images.

---

## 1. Fiche d'Identité & Modèle Commercial

| Champ | Valeur Stratégique |
| :--- | :--- |
| **Composant** | `mcp-03-media-quality-auditor` |
| **Pôle d'Appartenance** | **Pôle 2 : Suite E-Commerce & Ingestion de Catalogues Marchands** |
| **Modèle Business** | **OUTIL OPEN-SOURCE (Marketing Image & E-commerce)** |
| **Stratégie de Visibilité** | **CODE PUBLIC OPEN-SOURCE (MIT)** |
| **Potentiel Marché** | Génération de leads e-commerce sur LinkedIn. Détecte le flou, calcule le hash perceptuel et élimine les doublons d'images. |

---

## 2. Guide d'Installation 1-Clic (Développeur Humain)

```bash
git clone https://github.com/snorbik-ai/mcp-03-media-quality-auditor.git
cd mcp-03-media-quality-auditor
python install.py
```

Le script installe automatiquement les dépendances requises et résout les chemins de manière dynamique (**zéro chemin Windows absolu en dur**).

---

## 3. Configuration 1-Clic pour Agents IA (Cursor, Antigravity, Claude Code)

Ajoutez ce bloc à votre fichier `.mcp.json` ou `mcp_config.json` :

```json
{
  "mcpServers": {
    "mcp-03-media-quality-auditor": {
      "command": "python",
      "args": ["canal_mcp/mcp_server.py"],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      },
      "type": "stdio"
    }
  }
}
```

---

## 4. Catalogue Sémantique des Outils (`tools`)

| Outil (`name`) | Rôle & Fonction | Déclencheur d'Action (Quand l'appeler ?) | Arguments requis | Sortie Observable |
| :--- | :--- | :--- | :--- | :--- |
| `mcp_audit_media_library` | Scanne une bibliothèque d'images et repère les fichiers trop lourds ou flous. | **Avant toute campagne ou mise en ligne produit.** | `media_dir (str)` | Bilan de qualité et recommandations WebP |

---

## 5. Exemples Concrets de Prompts Utilisateur

Vous pouvez déclencher immédiatement ce composant en formulant ces requêtes dans votre IDE :

1. *« Audite les photos de la galerie pour repérer celles qui dépassent 500 Ko. »*
2. *« Trouve les images en doublon dans le dossier des médias produits. »*
3. *« Vérifie la netteté et la résolution des vignettes de garde-corps. »*

---

## 📜 Propriété & Licence
Composant officiel de l'écosystème **SNORBIK AI © 2026**.  
Tous droits réservés.

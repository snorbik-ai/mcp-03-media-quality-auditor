# 🤖 Prompt d'Installation Automatique pour Agent IA — Outil #03 — Contrôleur Qualité & Dédoublonneur Photos HD

> Ce fichier est destiné à être copié-collé directement dans le chat de votre assistant IA (Devin, Claude Code, Cursor, Windsurf, Antigravity IDE) pour installer, configurer et vérifier l'Outil #03 en un seul message.

---

`	ext
Tu es un agent d'ingénierie logicielle autonome chargé d'installer et de valider l'Outil #03 — Contrôleur Qualité & Dédoublonneur Photos HD.

RÉPERTOIRE CIBLE : outils_internes/03_media_quality_auditor/
MOTEUR TECHNIQUE : Python 3.10+ (Pillow)
RÔLE MÉTIER : Audite la netteté et la résolution des images, élimine les doublons par empreinte MD5 et certifie les photos candidates pour le Hero.

INSTRUCTIONS D'INSTALLATION ET DE PRISE EN MAIN :
1. Positionne-toi dans 'outils_internes/03_media_quality_auditor'.
2. Vérifie la présence des dépendances nécessaires ('requirements.txt' ou 'package.json') et installe-les si nécessaire.
3. Exécute la suite de tests officielle :
   python tests/run_all_suites.py
   Vérifie que 100 % des tests passent sans aucune erreur.
4. Pour enregistrer ce serveur MCP dans mon environnement :
   - Commande d'installation automatique :
     python ../install_mcp.py --tool 03
   - Ou ajoute manuellement dans la configuration MCP de l'IDE :
     Serveur : '03-media-quality-auditor'
     Commande : 'python'
     Args : ['outils_internes/03_media_quality_auditor/canal_mcp/mcp_classic_stdio/mcp_server.py']
5. Effectue un appel test JSON-RPC 'tools/list' pour confirmer que les outils sont bien exposés.
6. Résume en 3 points : statut des tests, outils MCP disponibles, et validation fonctionnelle.

RÈGLE DE SÉCURITÉ : N'effectue aucune opération destructive et n'expose aucun secret.
`

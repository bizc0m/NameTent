# Miss NameTent V2

Créez des chevalets porte-nom A4 avec noms, fonctions, logos et organisateur, puis exportez-les en PDF.

**[Ouvrir l’application](https://bizc0m.github.io/NameTent/)** · **[Télécharger le HTML autonome](https://github.com/bizc0m/NameTent/releases/latest/download/Miss-NameTent-V2.html)** · **[Code source](src/app.html)**

## Utiliser sans installation, même hors ligne

1. Téléchargez `Miss-NameTent-V2.html` depuis le lien ci-dessus.
2. Ouvrez-le dans un navigateur récent.
3. Saisissez vos participants, ajustez les logos et téléchargez le PDF.

Le fichier contient l’application, ses images intégrées et ses bibliothèques PDF, polices, ZIP et CSV : environ **1,64 Mo**. Aucune connexion n’est nécessaire à son fonctionnement. Les liens externes du glossaire nécessitent Internet.

Les noms, logos et projets sont traités dans le navigateur. Enregistrez votre projet ZIP avant de fermer : les préférences d’interface sont conservées lorsque le navigateur le permet, mais elles ne remplacent pas la sauvegarde du projet.

## Modes et commandes

Les modes **Express / Simple / Avancé** sont placés près du titre.

- **Express** : la barre d’actions contient uniquement **Télécharger**, en vert.
- **Simple** : **Ouvrir → Aperçu → Enregistrer → Télécharger**.
- **Avancé** : même barre, avec les réglages de précision supplémentaires.

**Ouvrir** restaure un projet ZIP. **Aperçu** génère un aperçu PDF. **Enregistrer** sauvegarde un projet ZIP. **Télécharger** exporte le PDF.

## Participants, logos et impression

- Saisissez un participant par ligne : `Nom, Fonction`. La première virgule sépare le nom de la fonction.
- Importez ou exportez les participants au format CSV.
- Utilisez les logos communs ou les logos propres à un participant.
- Réglez l’organisateur, les polices, les tailles et la mise en page.
- Pour les caractères absents des polices standard, importez une police TTF/OTF adaptée en mode Avancé.
- Imprimez le PDF en **A4 paysage**, **taille réelle 100 %**, **recto uniquement**, puis pliez les chevalets.

## Code source et reconstruction

- `src/app.html` : source de l’interface et de la logique métier. Ce fichier de développement référence les bibliothèques en ligne.
- `vendor/` : versions locales des quatre bibliothèques et leurs notices de licence.
- `scripts/build.py` : intègre ces bibliothèques dans le HTML.
- `index.html` : application autonome générée, utilisée par GitHub Pages et distribuée en téléchargement.

Depuis la racine du dépôt, avec Python 3 :

```sh
python3 scripts/build.py
```

Aucune installation de dépendances ni connexion réseau n’est nécessaire pour cette reconstruction. Modifiez `src/app.html`, puis reconstruisez `index.html`.

Pour un serveur local facultatif :

```sh
python3 -m http.server 8000
```

Ouvrez ensuite `http://localhost:8000/`. L’ouverture directe du fichier HTML fonctionne aussi.

## Intégrer dans une page

```html
<iframe
  src="https://bizc0m.github.io/NameTent/"
  title="Miss NameTent V2"
  width="100%"
  height="900"
  style="border:0"
  allow="downloads"
></iframe>
```

Si le site hôte impose un attribut `sandbox`, ses permissions doivent autoriser les scripts et les téléchargements. Vérifiez le téléchargement dans le contexte d’intégration choisi.

## Publication

GitHub Pages est configuré sur la branche **main**, dossier **racine**. Après une modification, reconstruisez le HTML et poussez les fichiers sur `main`. Les téléchargements de la release correspondent à la version publiée de cette release.

## Bibliothèques tierces

- pdf-lib **1.17.1** — MIT.
- @pdf-lib/fontkit **1.1.1** — MIT.
- JSZip **3.10.1** — MIT ou GPLv3 ; distribution utilisée sous MIT.
- Papa Parse **5.4.1** — MIT.

Les notices tierces sont conservées dans `vendor/`. Aucune licence supplémentaire n’est attribuée ici au code applicatif.

## Vérifications

La publication est vérifiée avec un navigateur automatisé : chargement de l’application, erreurs JavaScript et ressources, ordre et couleur des actions, export PDF dans les trois modes, ouverture de l’aperçu, sauvegarde ZIP et restauration des participants. Le fichier autonome est également testé en ouverture locale sans réseau.

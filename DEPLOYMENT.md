# Public Sandbox Deployment

This repository contains a static browser-only evaluator sandbox at the repository root: `index.html`.

## GitHub Pages

A GitHub Pages deployment workflow is included at:

```text
.github/workflows/deploy-pages.yml
```

To turn on the public site:

1. Open the repository **Settings** on GitHub.
2. Select **Pages** in the left navigation.
3. Under **Build and deployment**, choose **GitHub Actions** as the source.
4. Open the **Actions** tab and confirm that **Deploy public evaluator sandbox to GitHub Pages** completes successfully.
5. GitHub will display the public URL in the workflow environment or repository Pages settings.

The expected site address follows this pattern:

```text
https://kamanaka5502.github.io/creative-ops-ai-specialist-evaluation/
```

Do not send that URL until GitHub Pages shows that the deployment is active.

## Local preview

No dependency installation is required.

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

## Safety check before sharing

Before sharing publicly, confirm that the repository contains only the intended public evaluation materials and no credentials, customer content, private repository exports, or protected implementation artifacts.

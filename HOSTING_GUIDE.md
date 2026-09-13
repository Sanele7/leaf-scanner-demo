# Hosting Guide — Live Leaf Scanner Demo

Phone browsers require **HTTPS** to grant camera access (except on `localhost`).
GitHub Pages gives you free HTTPS hosting for both the model files and the demo
page itself, which is why it's the simplest option here.

## Step 1 — Create a GitHub repository

1. Go to github.com → New repository (e.g. `leaf-scanner-demo`)
2. Make it Public (GitHub Pages on free accounts requires this)

## Step 2 — Upload the converted model files

1. Run `convert_to_tfjs.py` in Colab (produces `mobilenetv2_tfjs.zip`)
2. Download and unzip it on your PC — you'll see `model.json` plus several
   `group1-shard*.bin` files
3. In your GitHub repo, create a folder called `model/`
4. Upload all those files into `model/` (drag-and-drop works on github.com,
   or use `git add` / `git push` if you're comfortable with git)

## Step 3 — Upload the demo page

1. Save the HTML file I've given you as `index.html`
2. Upload it to the **root** of the same repository (not inside `model/`)
3. Open `index.html` and find this line near the top of the `<script>` section:
   ```js
   const MODEL_URL = 'model/model.json';
   ```
   This already points at the right relative path if both are in the same repo
   — no change needed if you followed steps 2-3 exactly.

## Step 4 — Enable GitHub Pages

1. In your repo: Settings → Pages
2. Under "Source", choose **Deploy from a branch**
3. Branch: `main` (or `master`), folder: `/ (root)`
4. Save. GitHub will give you a URL like:
   `https://yourusername.github.io/leaf-scanner-demo/`
5. Wait 1-2 minutes for it to go live (GitHub shows a green checkmark when ready)

## Step 5 — Test on your phone

1. Open that URL directly on your phone's browser (Chrome or Safari)
2. Allow camera access when prompted
3. Point the rear camera at a leaf — predictions should start appearing within
   a second or two once the model finishes loading (a one-time ~25MB download,
   so the first load may take a moment on slower connections)

## Troubleshooting

- **"Camera access denied"** — check your phone's browser site settings; some
  browsers block camera access if you dismissed the permission prompt too
  quickly. Reload the page to get prompted again.
- **Model won't load / stuck on "Loading model..."** — open the page on a
  laptop first and check the browser console (F12 → Console tab) for the exact
  error. Usually means `MODEL_URL` doesn't match where the files actually are,
  or the shard files didn't fully upload.
- **Predictions look wrong / confidence always low** — double check you
  converted the *trained* model (`MobileNetV2_full.keras`), not an
  intermediate checkpoint from partway through training.

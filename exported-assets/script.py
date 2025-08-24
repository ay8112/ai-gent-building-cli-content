import zipfile
import os

# Create the folder structure in a temporary directory
dirs = [
    "YouTube-AI-Content-Package/script",
    "YouTube-AI-Content-Package/thumbnails",
    "YouTube-AI-Content-Package/video",
    "YouTube-AI-Content-Package/assets",
    "YouTube-AI-Content-Package/documentation"
]

files = {
    "YouTube-AI-Content-Package/README.md": "# YouTube AI Content Package\n\nComprehensive package for the project 'Shocking AI Tools Replacing Full-Time Jobs!'\n",
    "YouTube-AI-Content-Package/script/final_script.txt": "(Paste your final YouTube script here)",
    "YouTube-AI-Content-Package/thumbnails/concept_1_prompt.txt": "(Paste thumbnail concept 1 AI prompt here)",
    "YouTube-AI-Content-Package/thumbnails/concept_2_prompt.txt": "(Paste thumbnail concept 2 AI prompt here)",
    # final_thumbnail_design.png is to be added manually
    "YouTube-AI-Content-Package/video/invideo_project_link.txt": "(Paste InVideo/Pictory project link or export info here)",
    "YouTube-AI-Content-Package/assets/voiceover_suggestions.txt": "(List voiceover artist or AI voice suggestions here)",
    "YouTube-AI-Content-Package/assets/background_music_ideas.txt": "(Add background music or genre suggestions here)",
    "YouTube-AI-Content-Package/.gitignore": "*.png\n*.mp4\n*__pycache__*/\n.DS_Store\nThumbs.db\n",
    # The PDF will be added from attachment after creating base structure
}

# Make directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create files with template content
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Copy uploaded PDF into documentation folder
pdf_src = "Untitled-document.pdf"
pdf_dst = "YouTube-AI-Content-Package/documentation/project_overview.pdf"
import shutil
shutil.copy(pdf_src, pdf_dst)

# Zip the entire package
def zipdir(path, ziph):
    # Zipfile must have relative paths
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(path))
            ziph.write(file_path, arcname)

zipname = "YouTube-AI-Content-Package.zip"
with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('YouTube-AI-Content-Package', zipf)

zipname

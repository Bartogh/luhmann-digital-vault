import os
import shutil

def sync_vault():
    # Stier (Tilpas hvis din Obsidian vault ligger et andet sted)
    source_dir = "docs" 
    
    print(f"--- Synkroniserer Luhmann-arkiv ---")
    # Her kan vi tilføje logik til at rense tags eller formatere links
    # For nu bekræfter vi blot, at strukturen er klar til MkDocs
    if os.path.exists(source_dir):
        print(f"✅ Standby: {len(os.listdir(source_dir))} noter fundet.")
    else:
        print(f"❌ Fejl: docs-mappen blev ikke fundet.")

if __name__ == "__main__":
    sync_vault()
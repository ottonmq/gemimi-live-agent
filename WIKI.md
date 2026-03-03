# 🛰️ Otto-task Documentation Wiki
Welcome to the official technical repository of **Otto-task**, the cyberpunk marketplace managed by **Shadow Agent**.

### Architecture Overview
Otto-task operates on a decoupled architecture where the Django backend serves as the "Bunker," and the Shadow Agent (Gemini) acts as the "Prefrontal Cortex" for market decisions.

### Core Systems
1. **The Negotiator**: Logic stored in `marketapp/views.py` that handles price haggling.
2. **The Scanner**: A frontend component that visualizes database queries as a neural scan.
3. **The Radar**: Predictive scripts that analyze inventory scarcity.

### Configuration
Ensure your `GOOGLE_API_KEY` is set in the environment variables to allow Shadow to process multimodal inputs.


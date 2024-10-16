from flask import Blueprint, render_template, redirect, request, jsonify

analyze_recipe_bp = Blueprint('analyze_recipe', __name__, template_folder='templates')

@analyze_recipe_bp.route('/analyze_recipe', methods=['POST'])
def index():
    return jsonify({
        "id": "chatcmpl-AIo4zZk1UQamvWVIPiltTLoSsx5Gk",
        "object": "chat.completion",
        "created": 1729045773,
        "model": "gpt-4o-2024-08-06",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "### Tomato and Cheese Sandwich Recipe\n\n#### Ingredients:\n- 1 packet of tomatoes\n- 1 packet of cheese\n- 1 packet of bread\n\n#### Instructions:\n\n1. **Prepare Ingredients:**\n   - Wash the tomatoes thoroughly under running water.\n   - Slice the tomatoes into thin, even slices.\n   - Open the cheese packet and separate slices (or grate if using a block).\n\n2. **Assemble the Sandwich:**\n   - Take out 2 slices of bread from the packet.\n   - Lay one slice of bread flat on a clean surface or plate.\n   - Place a layer of tomato slices on top of the bread slice.\n   - Add cheese slices (or sprinkle grated cheese) on top of the tomatoes.\n   \n3. **Complete the Sandwich:**\n   - Place the second slice of bread on top of the cheese.\n\n4. **Toast the Sandwich (Optional):**\n   - Heat a non-stick pan on medium heat.\n   - Place the sandwich onto the pan and toast until the bread turns golden brown and the cheese melts, about 2-3 minutes per side. \n\n5. **Serve:**\n   - Remove the sandwich from the pan.\n   - Let it cool slightly and serve.\n   - Optionally, you can cut the sandwich in half for easier handling.\n\nEnjoy your tomato and cheese sandwich!",
                    "refusal": None
                },
                "logprobs": None,
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 72,
            "completion_tokens": 270,
            "total_tokens": 342,
            "prompt_tokens_details": {
                "cached_tokens": 0
            },
            "completion_tokens_details": {
                "reasoning_tokens": 0
            }
        },
        "system_fingerprint": "fp_6b68a8204b"
    })
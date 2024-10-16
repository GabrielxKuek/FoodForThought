from flask import Blueprint, render_template, redirect, request, jsonify

analyze_receipt_bp = Blueprint('analyze_receipt', __name__, template_folder='templates')

@analyze_receipt_bp.route('/analyze_receipt', methods=['POST'])
def index():
    return jsonify({
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gpt-4o-mini",
        "system_fingerprint": "fp_44709d6fcb",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Cheese, 1, Sausages, 1, Tomatoes, 1",
            },
            "logprobs": None,
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21,
            "completion_tokens_details": {
                "reasoning_tokens": 0
            }
        }
    })

@analyze_receipt_bp.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"
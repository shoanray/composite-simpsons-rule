from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


def safe_eval(expr: str, x: float) -> float:
    """Safely evaluate a mathematical expression with a given x value."""
    allowed_names = {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "log2": math.log2,
        "log10": math.log10,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "abs": abs,
    }
    try:
        return float(eval(expr, {"__builtins__": {}}, allowed_names))
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def composite_simpsons(f_expr: str, a: float, b: float, n: int):
    """
    Composite Simpson's 1/3 Rule.
    n must be even. Returns (result, steps_list).
    """
    if n % 2 != 0:
        raise ValueError("n must be even for Composite Simpson's 1/3 Rule.")
    if n < 2:
        raise ValueError("n must be at least 2.")

    h = (b - a) / n
    x_vals = [a + i * h for i in range(n + 1)]
    f_vals = [safe_eval(f_expr, x) for x in x_vals]

    # Build step-by-step data
    steps = []
    for i, (xi, fi) in enumerate(zip(x_vals, f_vals)):
        if i == 0 or i == n:
            coeff = 1
            label = "endpoint"
        elif i % 2 == 1:
            coeff = 4
            label = "odd"
        else:
            coeff = 2
            label = "even"
        steps.append({
            "i": i,
            "x": round(xi, 10),
            "fx": round(fi, 10),
            "coeff": coeff,
            "label": label,
            "weighted": round(coeff * fi, 10),
        })

    sum_all = sum(s["weighted"] for s in steps)
    result = (h / 3) * sum_all

    return {
        "result": result,
        "h": h,
        "n": n,
        "a": a,
        "b": b,
        "steps": steps,
        "sum_all": sum_all,
        "f_expr": f_expr,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        f_expr = data.get("f_expr", "").strip()
        a = float(data["a"])
        b = float(data["b"])
        n = int(data["n"])

        if not f_expr:
            raise ValueError("Function expression cannot be empty.")
        if a >= b:
            raise ValueError("Lower bound a must be less than upper bound b.")

        result = composite_simpsons(f_expr, a, b, n)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=False)

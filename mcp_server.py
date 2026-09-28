"""MCP stdio server for Gillespie SSA."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import GillespieSimulator

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "simulate_decay_process",
                        "description": "Exact Gillespie stochastic simulation of unimolecular decay A -> 0",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "initial_molecules": {"type": "integer"},
                                "rate_k": {"type": "number"},
                                "t_max": {"type": "number", "default": 10.0},
                                "seed": {"type": "integer", "default": 42}
                            },
                            "required": ["initial_molecules", "rate_k"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "simulate_decay_process":
            n0 = int(args.get("initial_molecules"))
            k = float(args.get("rate_k"))
            t_max = float(args.get("t_max", 10.0))
            seed = int(args.get("seed", 42))
            traj = GillespieSimulator.simulate_decay(n0, k, t_max, seed)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"trajectory": traj, "reactions_count": len(traj) - 1}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()

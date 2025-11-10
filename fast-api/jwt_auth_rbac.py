from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
import jwt, time

SECRET = "change-me"
auth = HTTPBearer()

def make_token(sub: str, role: str):
    return jwt.encode({"sub": sub, "role": role, "exp": int(time.time())+3600}, SECRET, "HS256")

def require_role(role: str):
    def dep(credentials = Depends(auth)):
        try:
            claims = jwt.decode(credentials.credentials, SECRET, algorithms=["HS256"])
        except Exception:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "bad token")
        if claims.get("role") != role:
            raise HTTPException(status.HTTP_403_FORBIDDEN, "forbidden")
        return claims
    return dep

@app.get("/admin/metrics")
def metrics(_: dict = Depends(require_role("admin"))):
    return {"ok": True}
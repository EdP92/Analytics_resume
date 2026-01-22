from __future__ import annotations

from typing import Any

import hmac
import streamlit as st


def _get_users() -> dict[str, dict[str, Any]]:
    users = {}
    try:
        if hasattr(st.secrets, "to_dict"):
            users = st.secrets.to_dict().get("users", {})
    except Exception:
        users = {}
    if not users:
        try:
            users = st.secrets["users"]
        except Exception:
            users = st.secrets.get("users", {})
    if isinstance(users, dict):
        return users
    return {}


def authenticate(username: str, password: str) -> bool:
    users = _get_users()
    if not users:
        st.error("Missing users in secrets. Add them to `.streamlit/secrets.toml`.")
        return False
    record = users.get(username)
    if not isinstance(record, dict):
        return False
    stored = str(record.get("password", ""))
    if not stored:
        return False
    if hmac.compare_digest(password, stored):
        st.session_state.authenticated = True
        st.session_state.auth_user = username
        st.session_state.auth_role = record.get("role", "viewer")
        return True
    return False


def require_auth() -> None:
    if not st.session_state.get("authenticated"):
        st.warning("Please log in to access this page.")
        st.page_link("Landing Page.py", label="← Go to Landing Page")
        st.stop()


def logout() -> None:
    for key in ("authenticated", "auth_user", "auth_role"):
        if key in st.session_state:
            st.session_state.pop(key)

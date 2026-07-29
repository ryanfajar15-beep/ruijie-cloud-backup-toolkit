# AI Review Rules

## Single Source of Truth

Selalu gunakan:

1. PROJECT_CONTEXT.md

Jika terjadi konflik dengan dokumen lain,
PROJECT_CONTEXT.md menang.

---

## Review Order

1. Architecture
2. ADR Compliance
3. Engineering Standards
4. SOLID
5. SRP
6. Dependency
7. Layering
8. Naming
9. Security
10. Regression
11. Production Readiness

---

## Forbidden

AI tidak boleh:

- mengubah arsitektur tanpa approval
- memindahkan module tanpa approval
- membuat hardcode path
- membuat business logic di Main Controller
- melanggar PROJECT_CONTEXT.md
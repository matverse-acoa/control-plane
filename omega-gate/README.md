# Omega Gate (Ω-GATE / PBSE)

Operador Constitucional & Firewall de Admissibilidade do MatVerse.

## Visão Geral

O **Omega Gate** é o núcleo decisório do MatVerse: um firewall constitucional que aceita somente fluxos compatíveis com o invariante **Science → Evidence**.

Cada submissão de hipótese e protocolo recebe um veredito determinístico:

- `PASS`
- `BLOCK`
- `SILENCE`
- `ESCALATE`

Todas as decisões são registradas com hash SHA3-256 e preparadas para ancoragem em ledger.

## Estrutura

```text
omega-gate/
├── README.md
├── LICENSE
├── constitution.md
├── admissibility_law.md
├── pbse/
│   ├── pbse_engine.py
│   ├── decision_rules.yaml
│   ├── audit_log/
│   └── tests/
├── contracts/
│   ├── omega_gate.sol
│   └── deploy/
├── ledger/
│   └── proofs/
├── api/
│   ├── main.py
│   └── schema_openapi.yaml
├── infra/
│   ├── docker-compose.yml
│   └── requirements.txt
└── docs/
    └── architecture.md
```

## Uso rápido

```python
from pbse.pbse_engine import PBSEngine

hypothesis = {
    "id": "HYP-001",
    "formal": True,
    "traceable": True,
    "evidence_hash": "abc123",
}
protocol = {
    "id": "PROTO-001",
    "auditable": True,
    "complete": True,
}

verdict = PBSEngine().judge(hypothesis, protocol)
print(verdict.decision, verdict.reason)
```

## Status

Pronto para evolução em produção com auditoria determinística local.

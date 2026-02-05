# Arquitetura do Omega Gate

1. **Entrada**: hipótese + protocolo.
2. **PBSE Engine**: aplica leis de admissibilidade.
3. **Veredito**: PASS/BLOCK/SILENCE/ESCALATE.
4. **Auditoria**: gera hash SHA3-256 + registro append-only.
5. **Ledger/Contrato**: pronto para ancoragem periódica.

## Princípios

- determinismo;
- fail-closed;
- rastreabilidade completa;
- evidência imutável por hash.

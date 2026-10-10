# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Techdim Architecture Decision Records

**Repositório Oficial:** `https://github.com/Techdimbr/techdim-architecture-decision-records`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Techdim Architecture Decision Records (ADRs)
- **Identificador (Slug):** `techdim-architecture-decision-records`
- **Categoria:** Governança de Engenharia & Documentação de Decisões Arquiteturais
- **Stack Tecnológica:** Markdown, Mermaid.js, Python 3 stdlib (Linter de ADRs), GitHub Pages
- **Objetivo Central:** Manter o acervo formal, imutável e auditável de decisões tecnológicas de software, infraestrutura e ciberdefesa da TECHDIM, estruturado conforme o padrão internacional de Michael Nygard.

### Casos de Uso Reais
1. **Auditoria de Conformidade e ISO 27001:** Apresentação formal para auditores das justificativas de escolhas de segurança.
2. **Onboarding de Novos Engenheiros:** Compreensão imediata do motivo pelo qual a stack foi desenhada dessa forma.
3. **Prevenção de Regressões Arquiteturais:** Bloqueio de refatorações inadvertidas que reintroduzam problemas já superados no passado.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/` e `04_INTELIGENCIA/`

```text
03_APLICACAO/src/
└── adr_linter.py                      # Linter em Python que valida formato, seções e status de cada ADR

04_INTELIGENCIA_DE_DESENVOLVIMENTO/ADR/
├── ADR-001-padrao-canonico-7-diretorios.md   # Decisão sobre estrutura decimal 00 a 06
├── ADR-002-governanca-zero-leaks.md          # Decisão sobre pre-commit hooks anti-vazamento
└── ADR-003-integracao-guardiao-gemini.md     # Decisão sobre orquestração Antigravity e Spark
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários do Linter de ADRs:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVAS REGRAS DE GOVERNANÇA -->
- [x] Linter estático que valida cabeçalho, status e seções obrigatórias (Contexto, Decisão, Consequências);
- [x] Suporte a diagramas Mermaid embutidos nativamente;
- [ ] Script de geração automática de sumário e índice remissivo (`INDEX.md`);
- [ ] Exportação automatizada de site estático para o GitHub Pages da organização.

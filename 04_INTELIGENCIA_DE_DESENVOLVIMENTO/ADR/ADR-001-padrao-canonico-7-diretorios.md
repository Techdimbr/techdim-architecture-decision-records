# ADR-001: Adoção da Estrutura Canônica em 7 Diretórios (00 a 06)

**Status:** Aprovada  
**Data:** 2026-10-10  
**Decisores:** Deivis Írio Mayer (Kether_1) · Central de Arquitetura TECHDIM  

---

## Contexto
Repositórios corporativos frequentemente sofrem com dispersão de documentação, mistura de código com mídias pesadas e falta de padronização entre projetos de diferentes linguagens.

## Decisão
Adotamos formalmente a arquitetura canônica decimal em 7 diretórios obrigatórios:
- `00_AUDITORIA/`: Integridade criptográfica SHA-256;
- `01_SOBRE_O_PROJETO/`: Visão de negócio e requisitos;
- `02_COMO_USAR/`: Operação e implantação;
- `03_APLICACAO/`: Código-fonte (`src/`) e testes (`tests/`);
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Decisões de arquitetura e contexto para IA;
- `05_VERSOES/`: Registro semântico de versões;
- `06_MIDIA/`: Banners e identidade visual.

## Consequências
- **Positivas:** Previsibilidade absoluta na navegação de qualquer repositório, facilidade de indexação por agentes de IA e clareza para auditorias externas.
- **Negativas:** Exige disciplina da equipe para manter arquivos em seus respectivos diretórios canônicos.

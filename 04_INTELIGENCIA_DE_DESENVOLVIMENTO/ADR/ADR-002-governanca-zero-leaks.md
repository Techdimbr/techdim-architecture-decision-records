# ADR-002: Implementação da Política de Barreira Zero Leaks

**Status:** Aprovada  
**Data:** 2026-10-10  
**Decisores:** Deivis Írio Mayer (Kether_1) · Central de Ciberdefesa TECHDIM  

---

## Contexto
O vazamento acidental de tokens de API, chaves privadas e arquivos `.env` em repositórios Git públicos é um dos vetores de invasão mais frequentes e danosos em engenharia de software.

## Decisão
Estabelecemos a barreira estrita Zero Leaks:
1. Arquivos `.env` reais, certificados `.pem` e caminhos absolutos locais (`/home/...`) são bloqueados no git pre-commit hook;
2. Disponibilização obrigatória de `.env.example` sanitizado;
3. Auditoria contínua via CI/CD no GitHub Actions antes de cada merge.

## Consequências
- **Positivas:** Eliminação de 100% dos riscos de vazamento acidental de segredos no GitHub público;
- **Negativas:** Desenvolvedores devem configurar variáveis de ambiente localmente sem commitar arquivos reais.

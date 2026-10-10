#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Techdim Architecture Decision Records - Linter Estático de Conformidade
Verifica se as ADRs seguem o padrão Michael Nygard com todas as seções obrigatórias.
"""

import sys
from pathlib import Path
from typing import List, Dict, Tuple

SECOES_OBRIGATORIAS = [
    "status",
    "contexto",
    "decis", # cobre decisão / decisao
    "consequ" # cobre consequências / consequencias
]

STATUS_VALIDOS = ["proposta", "aprovada", "rejeitada", "substituída", "substituida", "depreciada"]

def validar_adr(caminho: Path) -> Tuple[bool, List[str]]:
    conteudo = caminho.read_text(encoding="utf-8").lower()
    erros = []
    
    # 1. Verifica se tem título H1
    if not any(linha.startswith("# ") for linha in caminho.read_text(encoding="utf-8").splitlines()):
        erros.append("Falta título principal H1 (# Título)")

    # 2. Verifica seções obrigatórias
    for secao in SECOES_OBRIGATORIAS:
        if secao not in conteudo:
            erros.append(f"Seção obrigatória ausente: '{secao}'")

    # 3. Verifica se tem status válido declarado
    if not any(f"status: {s}" in conteudo or f"status:** {s}" in conteudo or f"status** : {s}" in conteudo or f"**status:**" in conteudo for s in STATUS_VALIDOS):
        erros.append("Status da ADR ausente ou não reconhecido")

    return len(erros) == 0, erros

def main():
    pasta_raiz = Path(__file__).resolve().parent.parent.parent
    pasta_adrs = pasta_raiz / "04_INTELIGENCIA_DE_DESENVOLVIMENTO" / "ADR"
    
    print("=" * 65)
    print("🏛️  TECHDIM ADR LINTER - AUDITORIA DE DECISÕES DE ARQUITETURA")
    print("=" * 65)
    
    if not pasta_adrs.exists():
        print(f"❌ Pasta de ADRs não encontrada em: {pasta_adrs}")
        sys.exit(1)
        
    arquivos_adr = list(pasta_adrs.glob("*.md"))
    if not arquivos_adr:
        print(f"ℹ️  Nenhuma ADR encontrada em {pasta_adrs}.")
        sys.exit(0)
        
    falhas = 0
    for adr in arquivos_adr:
        valido, erros = validar_adr(adr)
        icone = "✅" if valido else "❌"
        print(f"{icone} {adr.name:<45} : {'CONFORME' if valido else 'ERRO'}")
        if not valido:
            falhas += 1
            for e in erros:
                print(f"    ⚠️  {e}")
                
    print("-" * 65)
    if falhas == 0:
        print(f"✓ Todas as {len(arquivos_adr)} ADRs estão em conformidade com o padrão Nygard.")
        sys.exit(0)
    else:
        print(f"❌ {falhas} ADRs com pendências de formatação.")
        sys.exit(1)

if __name__ == "__main__":
    main()

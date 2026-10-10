#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o linter de ADRs.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from adr_linter import validar_adr

class TestADRLinter(unittest.TestCase):
    def test_adrs_cadastradas_sao_conformes(self):
        pasta_adrs = SRC_DIR.parent.parent / "04_INTELIGENCIA_DE_DESENVOLVIMENTO" / "ADR"
        self.assertTrue(pasta_adrs.exists())
        arquivos = list(pasta_adrs.glob("*.md"))
        self.assertGreaterEqual(len(arquivos), 3)
        for adr in arquivos:
            valido, erros = validar_adr(adr)
            self.assertTrue(valido, f"ADR {adr.name} possui erros: {erros}")

if __name__ == "__main__":
    unittest.main()

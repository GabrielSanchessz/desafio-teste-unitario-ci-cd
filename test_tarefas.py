#!/usr/bin/env python3
import unittest
from tarefas_crud import validar_data, Tarefa


class TestValidarData(unittest.TestCase):
    """Testes para validação de data"""
    
    def test_data_valida(self):
        """✅ Data em formato YYYY-MM-DD válido"""
        resultado = validar_data("2026-03-20")
        self.assertTrue(resultado)
    
    def test_data_invalida_formato(self):
        """❌ Data em formato inválido"""
        resultado = validar_data("20/03/2026")
        self.assertFalse(resultado)
    
    def test_data_fevereiro_invalida(self):
        """❌ 30 de fevereiro não existe"""
        resultado = validar_data("2026-02-30")
        self.assertFalse(resultado)
    
    def test_ano_bissexto(self):
        """✅ 29 de fevereiro em ano bissexto"""
        resultado = validar_data("2024-02-29")
        self.assertTrue(resultado)


class TestTarefa(unittest.TestCase):
    """Testes para a classe Tarefa"""
    
    def test_criar_tarefa_valida(self):
        """✅ Criar tarefa com dados válidos"""
        tarefa = Tarefa(1, "Estudar", "Python", "2026-03-20")
        self.assertEqual(tarefa.id, 1)
        self.assertEqual(tarefa.titulo, "Estudar")
        self.assertEqual(tarefa.descricao, "Python")
    
    def test_tarefa_remove_espacos(self):
        """✅ Espaços extras são removidos"""
        tarefa = Tarefa(2, "  Limpar  ", "  Casa  ", "2026-03-21")
        self.assertEqual(tarefa.titulo, "Limpar")
        self.assertEqual(tarefa.descricao, "Casa")


if __name__ == "__main__":
    unittest.main(verbosity=2)

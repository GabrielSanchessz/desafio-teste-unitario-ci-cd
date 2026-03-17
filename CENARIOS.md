# Cenários de Teste

## ✅ CRIAR TAREFA - Sucesso
- Título: "Estudar Python"
- Descrição: "Aprender conceitos"
- Data: "2026-03-20"
→ Resultado: Tarefa criada com ID incrementado

## ❌ CRIAR TAREFA - Erro
- Título vazio: ""
→ Resultado: Sistema rejeita

## ❌ CRIAR TAREFA - Erro
- Data inválida: "20/03/2026"
→ Resultado: Sistema pede nova data

## ✅ DELETAR TAREFA - Sucesso
- ID: 1 (que existe)
→ Resultado: Tarefa excluída

## ❌ DELETAR TAREFA - Erro
- ID: 999 (não existe)
→ Resultado: Mensagem de erro

## ✅ VALIDAR DATA - Sucesso
- Data: "2025-12-31"
→ Resultado: Válida

## ✅ VALIDAR DATA - Sucesso (Bissexto)
- Data: "2024-02-29"
→ Resultado: Válida

## ❌ VALIDAR DATA - Erro
- Data: "2026-02-30"
→ Resultado: Inválida
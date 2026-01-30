# AgentScope_Examples
AgentScope Examples

Este repositório contém exemplos práticos de uso do AgentScope para criação de agentes baseados em LLMs.

O objetivo é servir como um playground para testar:

agentes ReAct

memória de agentes

sistemas multi-agente

integração com MCP

modelos locais (Ollama) e APIs (Groq)

Arquivos
Installation_Agent_Scope.ipynb

Notebook de instalação e configuração do ambiente.

Use este primeiro.

Agent_Scope_Call_GROQ.ipynb

Exemplo simples de chamada de LLM usando Groq API.

Mostra como:

configurar API

criar um agente

enviar prompts

Agent_Scope_Memory.ipynb

Exemplo de agente com memória.

Mostra como:

o agente mantém histórico

usa interações passadas no raciocínio

agentscope_memory.db

Banco SQLite usado pelo exemplo de memória.

Guarda o estado do agente entre execuções.

Agente_Scope_MCP.ipynb

Exemplo de uso do MCP (Model Context Protocol).

Mostra como:

conectar agentes a ferramentas externas

usar contexto dinâmico

Multi_Agent_Scope_MCP.ipynb

Exemplo de sistema multi-agente.

Mostra:

vários agentes com papéis diferentes

orquestração entre agentes

ReAct_Agent_Example.py

Exemplo em Python puro de um ReAct Agent.

Mostra:

padrão Reason + Act

uso de ferramentas

integração com Ollama

Modelfile_gpt_oss_safe

Arquivo de configuração de modelo para Ollama.

Usado para criar um modelo local customizado.

Ordem recomendada

Installation_Agent_Scope.ipynb

Agent_Scope_Call_GROQ.ipynb

Agent_Scope_Memory.ipynb

ReAct_Agent_Example.py

Agente_Scope_MCP.ipynb

Multi_Agent_Scope_MCP.ipynb

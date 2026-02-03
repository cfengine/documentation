---
layout: default
title: AI agent
sorting: 5
---

The AI agent in Mission Portal allows you to explore your infrastructure using natural language queries.

- Integrates with common AI providers, including Google Gemini, OpenAI, Anthropic, and Mistral.
- Supports running local models, through Ollama or using an OpenAI compatible API.
- The model does not generate data directly, it generates SQL queries which are seamlessly executed against your database.
- The resulting tables / SQL queries can be saved as reports.
- The AI gets the context of your previous messages in the same chat, so you can refer back to things mentioned in the conversation.

**Security and privacy**

- Data (values) is never shared with the AI model provider, only schema and column names are sent along with your queries.
- The UI allows you to inspect and verify the generated SQL queries.
- SQL queries are run in read-only transactions.
- The use of AI and choice of model and provider is up to you.
  The feature must be enabled in the settings, and CFEngine Mission Portal communicates directly with the AI provider.

## Chat

Once configured, the AI agent is accessible in an easy to use chat interface.

![](images/ai-agent.png)

## Settings

In the new AI settings page, you can configure the AI agent to use different providers and models.

![](images/ai-settings.png)

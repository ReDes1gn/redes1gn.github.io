# RēDesign, Pricing

Last updated: 2026-08-23

## The tool itself: free

RēDesign is free and open source, MIT licensed. No account, no subscription, no seat
limit, no usage cap imposed by LunarWerx. Download a prebuilt release or build it from
source, either way, the application costs nothing to acquire or run.

- License: MIT (https://github.com/LunarWerxs/ReDesign/blob/main/LICENSE)
- Source: https://github.com/LunarWerxs/ReDesign
- Download: https://github.com/LunarWerxs/ReDesign/releases/latest
- Current version: 1.6.6

## What you actually pay for: your own AI API usage

RēDesign runs locally and calls out only to the AI provider APIs you configure with your
own keys. There is no LunarWerx billing layer in between: each provider bills you
directly, at that provider's own published rates, for the calls RēDesign makes on your
behalf.

| Item | Who charges | Notes |
| --- | --- | --- |
| RēDesign application | Nobody, free and MIT licensed | No account or subscription |
| Claude API calls | Anthropic, at your key's rate | Bring your own key |
| GPT API calls | OpenAI, at your key's rate | Bring your own key |
| Gemini API calls | Google, at your key's rate | Bring your own key |
| DeepSeek API calls | DeepSeek, at your key's rate | Bring your own key |
| Qwen API calls | Alibaba Cloud, at your key's rate | Bring your own key |
| Any other OpenAI-compatible model | That provider, at your key's rate | Added via JSON config |

RēDesign does not mark up, resell, or take a cut of any of these API calls. You supply
the key, the provider bills you, and RēDesign is only the client making the request.

## Trying it for $0

Add `--mock` to a run and RēDesign skips real model calls entirely. The full flow works
end to end at zero API cost, useful for evaluating the tool before spending anything on
model usage.

## Cost visibility before and after a run

RēDesign shows a cost estimate before you hit Run and tracks an actual per-run cost meter
afterward, so a large fan-out across several models, or several variants per model in one
run, does not produce a surprise bill. There is no built-in spend cap; the estimate and
meter are informational, and your own provider account limits are the real backstop.

## For agentic / automated buyers

- No paid tiers, no license key to purchase, no usage-based fee from LunarWerx to budget
  for.
- The only recurring cost a deployment incurs is whatever AI provider API usage it
  generates, governed entirely by the API keys it is given.
- `--mock` gives a zero-cost integration test path.
- Full CLI (`bun run src/index.ts run|models|keys|mcp`) and an MCP server are included at
  no extra cost, for scripting or agent-driven runs.

## Links

- Full brief: https://redesign.lunarwerx.com/llms-full.txt
- Home: https://redesign.lunarwerx.com/
- Source: https://github.com/LunarWerxs/ReDesign

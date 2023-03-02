# Bypassing Server-side Paywalls
## Introduction
Web application developers may use paywalls to restrict website visitors from accessing paid news content. Paid news content can be accessed by visitors through paying a fee, or signing up for a paid subscription plan. The purpose of a paywall varies per news agency. The most common purpose is to get visitors to pay for paid content digitally; identical to buying a newspaper. This repository describes the types of paywalls that exist, but will focus on how to bypass server-side paywalls.

## Types of Paywalls
3 types of paywalls exist, namely:
- 'soft' paywall: implemented in the frontend of the web application, often tracked by using cookies that a visitor can manipulate.
- 'hard' a.k.a. server-side paywall: implemented server-side of the web application. Visitors must make a payment before they're allowed to see the paid content.
- 'metered' paywall: a mix of the above. Visitor can read a set number of paid articles for free before they must make a payment.

## How Server-side Paywalls Work
Server-side paywalls check if the visitor has made payment before the paid content is displayed. The breakdown of this logic looks like the below pseudocode:
```
if (visitor = paid_visitor) {
  // show paid content
} else {
  // show paywall
}
```

## The Flaw
Paywalled content must still be crawled by web crawlers, and indexed by search engines for it to be found by potential visitors. Web crawlers, in most cases, get full access to paywalled content. This is important for SEO purposes, relevance, and visibility. However, when the paywalled content gets crawled, a copy of the full content is cached by the web crawler. The paywalled content is then cached on internet archives. A visitor can now access the paywalled content on an internet archive without having paid a fee, or a subscription plan.

## Manual steps
1. Copy the URL that contains the paywalled content.
2. Visit internet archive of your choosing.
3. Open the desired cache of the URL.
4. You now have access to paywalled content.

## Proof-of-concept
A python script written in Python 3.6 is included in this repository. The python script automates the process of searching for the cache of paywalled content and returns the cache URLs.

![Executing the proof-of-concept script](https://github.com/stefanhesselman/paywall-bypass/blob/main/poc.gif?raw=true)

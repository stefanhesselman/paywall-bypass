# Bypassing Server-side Paywalls

## Types of Paywalls
3 types of paywalls exist, namely:
- 'soft' paywall: implemented in the frontend of the web application, often tracked by using cookies that a visitor can manipulate.
- 'hard' a.k.a. server-side paywall: implemented server-side of the web application. Visitors must make a payment before they're allowed to see the paid content.
- 'metered' paywall: a mix of the above. Visitor can read a set number of paid articles for free before they must make a payment.

## How Server-side Paywalls Work
Hard paywalls check if the visitor has made payment, is logged in, or has an active subscription before the paid content is displayed. The breakdown of this logic looks like the below pseudocode:
```
if (visitor = paid_visitor) {
  // show paid content
} else {
  // show paywall
}
```

## The Flaw
Paywalled content must still be crawled by web crawlers, and indexed by search engines for it to be found by potential visitors. Web crawlers, in most cases, get full access to paywalled content. This is important for SEO purposes. However, when the paywalled content gets crawled, a copy of the full content is cached by the web crawler. The paywalled content is then cached on internet archives. A visitor can now access the paywalled content on an internet archive without having paid a fee, or pay for a subscription plan.

## Manual steps
1. Copy the URL that contains the paywalled content.
2. Visit internet archive of your choosing.
3. Open the desired cache of the URL.
4. You now have access to the content without a paywall.

## Proof-of-concept
A python script written in Python 3.6 is included in this repository. The python script automates the process of searching for the cache of paywalled content and returns the cache URLs. It uses the website archive.is for this purpose.

![Executing the proof-of-concept script](https://github.com/stefanhesselman/paywall-bypass/blob/main/poc.gif?raw=true)

# Future work
Automate the webcrawling process in the event the target URL has not been archived yet.

## Note
No websites were attacked and no vulnerabilities were exploited in making this script. It merely shows how paywalls can be circumvented via legitimate resources.

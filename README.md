# ShorterUTM

Use smaller UTM parameters and improve the appearance of your link. ShorterUTM uses just one number to summarize all your UTM parameters used on your website for marketing campaigns. Here's an example of how to use it in Python:

```python
from shortutm import ShorterUTM

# Create a short code from UTM parameters
short_code = ShorterUTM.short(
    source="google",
    medium="cpc",
    campaign="black_friday",
    term="promoção",
    content="banner_01"
)

print(f"Generated code: {short_code}")

# Somewhere else (or in the future), restore the UTM parameters
utm_params = ShorterUTM.restore(short_code)

print("Restored params:")
print(utm_params)
```

## 🔁 Comparison: With 'ShorterUTM' vs Without ShorterUTM

#### ❌ Without ShortUTM

```
https://meusite.com/produto?utm_source=google&utm_medium=cpc&utm_campaign=black_friday&utm_term=promoção&utm_content=banner_01
```

#### ✅ With ShortUTM

```
https://meusite.com/produto?sutm=384917
```

--- 

Please read the license before using this project! This is a project created primarily for study reasons, **consider utilizing another database** when utilizing ShorterUTM.

# Session 08 - Specification Driven Testing

**Student:** Geetanshi Tinker  
**ID:** 25BCON2006

This project demonstrates writing tests from requirements rather than writing tests only to match an implementation.

## Specification
- Negative order total raises `ValueError`.
- 0 to 49.99 gets 0% discount.
- 50 to 99.99 gets 5%.
- 100 to 199.99 gets 10%.
- 200 and above gets 15%.
- VIP customers receive an additional 5 percentage points.
- Total discount rate is capped at 20%.

Run:
```bash
python -m unittest discover -s HW -p "test_*.py"
```

The important lesson is that passing tests are meaningful only when the tests represent the intended specification.

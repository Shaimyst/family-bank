# Family Bank: Path to a Real Product

## Context

The current app is a functional single-family MVP: a Streamlit app with hardcoded accounts (Willow, Penny), hardcoded parent passwords, and a flat JSON file for storage. The goal is to identify what it would take to turn this into a real, multi-family web service — with product, tech, and business recommendations.

---

## Current State (Strengths to Preserve)

- Dead-simple UX: select child, enter amount, parent authenticates, done
- Core domain model is correct: Transactions are immutable, balance is derived
- Chores → allowance workflow is the right narrative hook
- MIT licensed, clean codebase

---

## Product Recommendations

### Phase 1: Make it shareable (private beta)
- **Multi-family accounts**: Replace hardcoded accounts with proper user registration. Each family is isolated from others.
- **Dynamic child/parent accounts**: Let families add their own children and parents — not hardcoded Willow/Penny/Dada/Mamma.
- **Transaction history UI**: Display per-child transaction log with dates, amounts, descriptions.
- **Child-facing view**: A read-only view (possibly with a PIN) where kids can see their own balance and history. Huge motivational value.

### Phase 2: Make it sticky
- **Savings goals**: Kids set a goal (e.g. "Nintendo Switch - $300"). App shows progress. This is the single highest-value feature for engagement.
- **Scheduled recurring allowances**: Set a weekly/monthly automatic credit — removes the manual "I forgot to pay allowance" problem.
- **Chore tracking**: Link chores to pending payments. Parent marks chore done → payment queued for approval.
- **Interest rates**: Teach kids compound interest by offering a configurable "savings rate" on balances.

### Phase 3: Expand the product surface
- **Spending categories**: Tag transactions (food, toys, savings, charity). Pie charts for kids to see spending patterns.
- **Email/push notifications**: Notify kids when money arrives. Notify parents when balance is low.
- **Parent dashboard**: Aggregate view across all kids — total balances, recent transactions, upcoming scheduled payments.
- **Export**: Download CSV/PDF of transaction history (useful for tax/gift tracking).

---

## Tech Recommendations

### Immediate (before any real users)

1. **Move secrets to environment variables**: Password hashes and any future credentials must NOT be hardcoded in source. Use `.env` + `python-dotenv` or a secrets manager.

2. **Replace JSON with a real database**: SQLite is fine for early stage. PostgreSQL when you go multi-user. ORM: SQLAlchemy or the lighter `sqlite-utils`. Schema:
   - `families` (id, name, created_at)
   - `parents` (id, family_id, name, password_hash)
   - `children` (id, family_id, name, created_at)
   - `transactions` (id, child_id, parent_id, amount, description, created_at)

3. **Proper session/auth**: Replace per-transaction password entry with a real login session. Use `streamlit-authenticator` for quick wins, or migrate to a real framework.

### Medium-term (first real users)

4. **Containerize with Docker**: A `Dockerfile` + `docker-compose.yml` makes deployment portable and reproducible.

5. **Cloud hosting**: Easiest paths:
   - **Streamlit Community Cloud** (free, fast to deploy, but limited — no persistent DB)
   - **Railway or Render** (~$5-7/month, supports PostgreSQL, custom domains, auto-deploy from GitHub) — recommended starting point
   - **Fly.io** (more control, generous free tier)

6. **CI/CD**: GitHub Actions for running tests on every push and auto-deploying to hosting on merge to main.

7. **Tests**: The codebase currently has zero tests. Priority:
   - Unit tests for `Transaction` and `ChildAccount` (especially the "balance can't go negative" rule)
   - Integration tests for the database layer
   - Use `pytest`

### Longer-term (growth)

8. **Migrate from Streamlit to a proper stack** if you need mobile support, custom design, or performance:
   - **Backend**: FastAPI (Python, reuse existing logic)
   - **Frontend**: Next.js or a React SPA
   - **Auth**: Supabase Auth or Auth0 for free-tier OAuth

9. **Mobile**: React Native or Flutter — or just ensure the web app is mobile-responsive (Streamlit is passable on mobile but not great).

10. **Backups**: Automated daily DB dumps to S3 or similar. Non-negotiable once real families rely on it.

---

## Business Recommendations

### Who is this for?
- **Primary**: Parents of children aged 5-14 who want to teach financial literacy
- **Secondary**: Families with teenagers learning to budget
- **Sweet spot**: Parents who are tech-comfortable but want something simpler than spreadsheets and more tangible than cash

### Competitive landscape
- **Greenlight** / **GoHenry** / **BusyKid**: These are debit card products (~$5-10/month). High trust bar, regulated.
- **Homey** / **OurFamilyWizard**: Chore apps that bolt on payments.
- **Your edge**: Zero fees, no physical card (lower complexity), transparent (you can see/own the code), customizable for your family's values.

### Business model options

**Option A: Open source / self-hosted (no business, but high credibility)**
- Keep MIT license, publish on GitHub, write a good README
- Build a reputation as the "family bank for engineers"
- Monetize via consulting, sponsorships, or "managed hosting" tier

**Option B: Freemium SaaS**
- Free: 1 family, 2 kids, basic features
- Paid ($3-5/month): unlimited kids, goals, recurring allowances, notifications, export
- Low-cost, recurring revenue. Simple to explain.

**Option C: One-time purchase**
- Sell a polished desktop/web app for a flat fee ($15-25)
- No ongoing commitment, easier to start — but no recurring revenue

**Recommended starting path: Option A → B**
1. Open-source it properly with great docs
2. Let other tech-savvy parents self-host
3. Build an audience (parenting communities, Hacker News, Product Hunt)
4. Add a managed hosted version as a paid tier once there's demand

### Go-to-market
- **Communities**: r/personalfinance, r/Parenting, Hacker News "Show HN", indie maker communities (Indie Hackers)
- **Content**: "How I built a bank for my kids" blog post is a natural viral piece
- **Product Hunt launch**: Aim for a polished free tier first
- **School/org partnerships**: Financial literacy programs, credit unions, teachers — potential B2B2C angle

### Legal/compliance note
- As long as you're NOT holding real money (this is a ledger/tracker, not a payment processor), you avoid most financial regulations
- If you ever want real card/payments integration, you'd need to partner with a licensed entity (like Stripe Treasury or a BaaS provider)
- Privacy policy + Terms of Service required once you have real users, especially regarding children's data (COPPA in the US)

---

## Prioritized Roadmap

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Move secrets to env vars | 1 hour | High (security) |
| 2 | Add transaction history display | 2-3 hours | High (UX) |
| 3 | Replace JSON with SQLite | 1 day | High (scalability) |
| 4 | Dynamic child/parent creation | 1 day | High (multi-family) |
| 5 | Docker + Railway deploy | 1 day | High (shareable) |
| 6 | Savings goals feature | 2 days | Very High (stickiness) |
| 7 | Child read-only view | 1 day | High (engagement) |
| 8 | Write tests | 1-2 days | Medium (maintainability) |
| 9 | Recurring allowances | 2 days | High (stickiness) |
| 10 | Product Hunt launch | 1 week | Variable (growth) |

---

## Files to Modify (when implementing)

- `app.py` - core application (needs significant refactoring for multi-family)
- `pyproject.toml` - add new dependencies (sqlalchemy, python-dotenv, pytest, etc.)
- New: `models.py` - SQLAlchemy models
- New: `auth.py` - session management
- New: `Dockerfile` + `docker-compose.yml`
- New: `.env.example`
- New: `tests/`

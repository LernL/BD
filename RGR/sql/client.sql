BEGIN;

TRUNCATE TABLE public.client RESTART IDENTITY CASCADE;

WITH emails AS (
  SELECT email, row_number() OVER () AS id
  FROM public.contacts_client
  ORDER BY random()
  LIMIT 100000
),
waiters AS (
  SELECT phone_num_w, row_number() OVER () AS id
  FROM public.waiter
  ORDER BY random()
  LIMIT 100000
)
INSERT INTO public.client (phone_num_w, email, phone_num_cl)
SELECT 
  w.phone_num_w,
  e.email,
  (random() * 1000000000000 + 1000000000)::bigint
FROM emails e
JOIN waiters w USING (id);

COMMIT;

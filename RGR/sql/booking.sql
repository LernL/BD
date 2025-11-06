BEGIN;

TRUNCATE TABLE public.booking RESTART IDENTITY CASCADE;

WITH numtb AS (
  SELECT num_table, row_number() OVER (ORDER BY random()) AS rn
  FROM public."table"
  LIMIT 100000
),
numcl AS (
  SELECT phone_num_cl, row_number() OVER (ORDER BY random()) AS rn
  FROM public.client
  LIMIT 100000
)
INSERT INTO public.booking (id, time_book, end_time, num_table, phone_num_cl, people_num)
SELECT
  row_number() OVER (ORDER BY random()) AS id,
  s.time_book,
  LEAST(24, s.time_book + (floor(random() * (24 - s.time_book))::int + 1)) AS end_time,
  s.num_table,
  s.phone_num_cl,
  s.people_num
FROM (
  SELECT nt.num_table, nc.phone_num_cl,
         (floor(random()*24)::int + 1) AS time_book,
         (floor(random()*8)::int + 1)  AS people_num,
         nt.rn
  FROM numtb nt
  JOIN numcl nc USING (rn)
) s;

COMMIT;

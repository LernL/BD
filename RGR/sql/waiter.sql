BEGIN;
TRUNCATE TABLE public.waiter RESTART IDENTITY CASCADE;
INSERT INTO public.waiter (name, phone_num_w)
SELECT chr(trunc(65+random()*25)::int) || Lower(chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) )  AS name,
   	   (random()*1000000000000)+1000000000::bigint
FROM generate_series(1,100000);

COMMIT;

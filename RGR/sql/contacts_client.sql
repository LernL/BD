BEGIN;
TRUNCATE TABLE public.contacts_client RESTART IDENTITY CASCADE;
INSERT INTO public.contacts_client (email, name)
SELECT Lower( chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || '@' ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) ||  chr(trunc(65+random()*25)::int) || '.com' )  AS name,
	chr(trunc(65+random()*25)::int) || Lower ( chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) )
FROM generate_series(1,100000);

COMMIT;

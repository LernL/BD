BEGIN;

TRUNCATE TABLE public.table RESTART IDENTITY CASCADE;

WITH params AS (
  SELECT
    ARRAY['wood','metal','plastic','glass','stone'] AS materials,
    ARRAY['square','circle','rectangle','oval']       AS shapes
)

INSERT INTO public.table (num_table, number_chairs, material, table_shape)
SELECT
  gs AS num_table,                                      
  (floor(random()*8) + 1)::int AS number_chairs,        
  params.materials[(floor(random()*array_length(params.materials,1)) + 1)::int] AS material,
  params.shapes[(floor(random()*array_length(params.shapes,1)) + 1)::int]       AS table_shape
FROM generate_series(1, 100000) AS gs                      
CROSS JOIN params;

COMMIT;

PGDMP     #    &                x            gsm_dev_test %   10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)    11.5     b           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            c           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            d           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            e           1262    16384    gsm_dev_test    DATABASE     ~   CREATE DATABASE gsm_dev_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE gsm_dev_test;
             postgres    false            �            1259    24287    processor_brand    TABLE     �   CREATE TABLE public.processor_brand (
    id integer DEFAULT nextval('public.processor_brand_id_seq'::regclass) NOT NULL,
    name text NOT NULL,
    is_active boolean DEFAULT true
);
 #   DROP TABLE public.processor_brand;
       public         postgres    false            _          0    24287    processor_brand 
   TABLE DATA               >   COPY public.processor_brand (id, name, is_active) FROM stdin;
    public       postgres    false    205   �       �
           2606    28064 $   processor_brand processor_brand_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.processor_brand
    ADD CONSTRAINT processor_brand_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.processor_brand DROP CONSTRAINT processor_brand_pkey;
       public         postgres    false    205            _   0   x�3�,M�I����,�2��MM�L,I�r�9�s�K�ҁ�=... �0     
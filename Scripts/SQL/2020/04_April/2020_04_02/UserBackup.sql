PGDMP         $                x            gsm_dev_test %   10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)    11.5     h           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            i           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            j           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            k           1262    16384    gsm_dev_test    DATABASE     ~   CREATE DATABASE gsm_dev_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE gsm_dev_test;
             postgres    false            �            1259    28164    user    TABLE     �   CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(100) NOT NULL
);
    DROP TABLE public."user";
       public         postgres    false            �            1259    28162    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public       postgres    false    209            l           0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
            public       postgres    false    208            �
           2604    28167    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    208    209    209            e          0    28164    user 
   TABLE DATA               ?   COPY public."user" (id, username, email, password) FROM stdin;
    public       postgres    false    209   �       m           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 1, true);
            public       postgres    false    208            �
           2606    28173    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public         postgres    false    209            �
           2606    28175    user user_password_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_password_key UNIQUE (password);
 B   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_password_key;
       public         postgres    false    209            �
           2606    28169    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public         postgres    false    209            �
           2606    28171    user user_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_username_key;
       public         postgres    false    209            e   w   x��;�0 �99G�*Nj'��!Y�Ħ�O*�@���=0U>��.��Z��r�����m��KU?�g�H�;u��s����!�:��.a
	TT#gp0D���DR�,N�YJb{뭵!%�     
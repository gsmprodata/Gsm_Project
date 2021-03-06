PGDMP         '                x            gsm_dev_test %   10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)    11.5     c           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            d           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            e           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            f           1262    16384    gsm_dev_test    DATABASE     ~   CREATE DATABASE gsm_dev_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE gsm_dev_test;
             postgres    false            �            1259    24277 	   processor    TABLE     �   CREATE TABLE public.processor (
    id integer DEFAULT nextval('public.processor_id_seq'::regclass) NOT NULL,
    name text NOT NULL,
    processor_brand_id integer,
    is_active boolean DEFAULT true
);
    DROP TABLE public.processor;
       public         postgres    false            `          0    24277 	   processor 
   TABLE DATA               L   COPY public.processor (id, name, processor_brand_id, is_active) FROM stdin;
    public       postgres    false    203   l       �
           2606    28066    processor processor_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.processor
    ADD CONSTRAINT processor_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.processor DROP CONSTRAINT processor_pkey;
       public         postgres    false    203            �
           2606    28134 +   processor processor_processor_brand_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.processor
    ADD CONSTRAINT processor_processor_brand_id_fkey FOREIGN KEY (processor_brand_id) REFERENCES public.processor_brand(id);
 U   ALTER TABLE ONLY public.processor DROP CONSTRAINT processor_processor_brand_id_fkey;
       public       postgres    false    203            `   �  x�mZ]r�~��S���?�$[v٣���J*׾L��=e��F�c�"�r��`�����z$@�A?��l���������}��_���U�1�y�Sц1OF�cr<\^���������-�Ti1%�ӜmVG��_\��w�n�|���ָ��НkF���.�����k�~���]�V��jbH,B�*WB��������u�>�)إ�#�j� �^I�G�m��XI1ǧ�H¬a�ϼ�ME�̪����M�u?b�Y:P��\C�����*/w�C�`D�q8�������si�)G���?�/��Ж]d��4���ˏ.;����-k���vۛ����	��!�=��.Tx��o�nw�L���q�p/��*�#���.���6m3k-6��mB�&R�	Ck��<���Y��Ⱥ��.�7>߽����s�y6�����Y�HڜZD�j�5��B�W���c��۹�8:<lo�㕳(���~�G�ar;�%Fn�њ�~	)�"��N1�w��8���^�m����~}dOEr^��*+1��U|lȍL�~(P�;���~��/��3L�C�|蟯�	��n#!�_�.�D�@1�Sw����?�~vd�c�w.HR9������ĳ�Z���X+p1����ˑ��m|�[&�`s�)��v��lXd�`�!�b'G����j��y���4����֊�M�u:�ńc!�հ>TyA���̽���b�^����|��b���d3������[>��}B�n�y���Z�w>���ؕ�������-*��{4B�����iw�|}�|/�B;�z/�8?�8�����,9캏��9z�g�A��4OJ�\ cJ~u��IުC�� �5����u˹�@D�>Y�d9d�PQ(��|�B�3�R|(��B�vq�}��v���ö�B��L��i|!�{�p�
��v��ȕ�PUw.�4O�'"g��}tV��U��,��?ÕP|]��@�����_���u��%6ñz�����@a`t�+��S�&PJWJ
U (�F�qdqX���������á�c�-e�V1�.��*]�J�*�(���O0}md`@nX�C�&(97�"T����*�^Bldq�����Ha_��z:G`�y��ݾ�`/Ģ��3�B�JpD�[t��)y�h���K@6)�b���}wKJ:�mo�����>�_;��b��o>������j�~ �8��8���I��9��Ii�(K>����,OE��O?⌙�lx���S&�/�\�,�9e[>�3��j�̀<��\�l��ا�+��zRV�hu�SYLOJqX�FS)�ObG�9�R��$��Z��M����%���F3��ͷFiJ��Mק	�p*�!\��;K���%������m�VJ�)�.��<����?�c�Qb�;�zW9���Ij�Z�)�N���VYn����G�q�|\�]�?� !٥#�De����4ҕ<�7IWݦ��������"�\ӃDc�FT+���5���0������%Gk�Rte0z��a�k�.��v������6zM����F-���=|UN
ǫ& ��ӯucs=(+�2�rT�p�io�J�=`����t�Lk#qA�-�$o�z�L5�a�G����%S%��������sS�^���jf�z�G	;�MZX)0��:�֜�߾쯻�bL�X>,|������g*��Ã2�� ��J�)GP��m��Qߡ�b_��(Po�RU��V޼�ꤖbJ�Z�uv��<G�N��?\�;�}޾>y��v�\�ȩ*ύ��ԑ�1\T(b!Oc�0&�	}=Ł9zѣ��W���D��bI�I1�ͧ
����S<���з_|ĥ ������R��4��_�J�@�V��4�l(c��2f~F���d,h�oG�@'�Fz#Hh��b���H�V�d��o��a��3rENwA�кb*�59E����� � �D�����s�M�(�q��<��(>G%��\T
g�!�Z��}R �*��O�ny����Xע����M��.�m-e��G�E�^�`��E~�E�=��:1�q�SӉ5-	�|�
�"m�+��q즄Z�ly�[2��%$�5cs�,d�Z�)�5�a�J������׏�����U�G����n㌤
�a
!��/ ���tf�`?�2��^��Մ�T����/y�1̣p��`ک���I���ʒ��+�1�I*�K��F������yA�ʛ���	M���]뼡��C�$�9rZ�S��Jk\�M��eW�f�7>��_�ϩ�9�Njg����ixR+�ܴ	]� $j�����6oJn��1����6k"[�����6rng2�}t#�]#�S!}��^��Of�f�Y/���m�!���Ϗ�����~\PB��r�,��l�H��5;�)���ƕ�����W�r����VȂ@�y��K���w2��>�eۣ��N�[�|�2��v��󻀇 �O9}�b�R���J�̉C���FE�ua�6�L�՞<�4�C&�4�|?J�6TY\	@LZ
�d0�����	���%�0��$�Д�Y7�~��zM{1O�ݺ�]�_�ݳ���eJ,�
��I>L��P}ω�u&�#�ϖ�z$�)�����,��}�I��&2257_LV�h#R��iwPɭK9��������[
����=�8�9q=vU��N -X��^p2�z~���9��<t��GJ�Q�D?	�h��<R{���*�?3��2�"����P1��+�������r����L{r!�K'�K'�TiSD��K�E��1K,]�"��*+�=Z}h����"����@-�� u���Ѭ��V���rUऄ��;�'jۧ o��ȁ��J��- �$�y�(��RxA�V��6����\�y����� 2�*�����;�1�&�i҄��/��TD��خl.��#ۡ�^ZP&}��h�;K0rb2�f�[�BH%i��ȁ$��Ș%�\�4�A�_��R�fԱ��O��Kj��~5�h�
'BN�4�F��Y�O����3q��+adY��*��A�P�K�ߛG�`�'ĬW\Y#�����碛P����;�M�^8��\���h��݁<���[��w�'n+��4�'�ŮV~�@�ʳ�vM䙽���<�;���~��_=��6c:���̋��&���!�������^��?{�a�     
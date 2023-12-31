PGDMP                       |            System    16.1    16.1 $    
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24590    System    DATABASE     �   CREATE DATABASE "System" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "System";
                postgres    false            �            1259    24612    cases    TABLE     ,  CREATE TABLE public.cases (
    open_case_id integer NOT NULL,
    status character varying(20),
    fraudaccount_id integer,
    fraudtransaction_id integer,
    CONSTRAINT cases_status_check CHECK (((status)::text = ANY ((ARRAY['close'::character varying, 'open'::character varying])::text[])))
);
    DROP TABLE public.cases;
       public         heap    postgres    false            �            1259    24611    cases_open_case_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cases_open_case_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.cases_open_case_id_seq;
       public          postgres    false    216                       0    0    cases_open_case_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.cases_open_case_id_seq OWNED BY public.cases.open_case_id;
          public          postgres    false    215            �            1259    24639    fraudaccounts    TABLE     I  CREATE TABLE public.fraudaccounts (
    fraudaccount_id integer NOT NULL,
    customer_id integer,
    first_name character varying(50),
    last_name character varying(50),
    account_balance numeric(15,2),
    age integer,
    address text,
    mobileno character varying(15),
    addharno character varying(12),
    lastlogin date,
    branchid integer,
    account_type character varying(20),
    emailid character varying(50),
    upi_id character varying(50),
    account_number character varying(20),
    pancard_number character varying(15),
    city character varying(50)
);
 !   DROP TABLE public.fraudaccounts;
       public         heap    postgres    false            �            1259    24638 !   fraudaccounts_fraudaccount_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fraudaccounts_fraudaccount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.fraudaccounts_fraudaccount_id_seq;
       public          postgres    false    220                       0    0 !   fraudaccounts_fraudaccount_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.fraudaccounts_fraudaccount_id_seq OWNED BY public.fraudaccounts.fraudaccount_id;
          public          postgres    false    219            �            1259    24648    fraudtransactions    TABLE     F  CREATE TABLE public.fraudtransactions (
    fraudtransaction_id integer NOT NULL,
    transactionid integer,
    transactiontype character varying(20),
    amount_before_transaction numeric(15,2),
    amount_after_transaction numeric(15,2),
    transaction_date date,
    from_account_id integer,
    to_account_id integer
);
 %   DROP TABLE public.fraudtransactions;
       public         heap    postgres    false            �            1259    24647 )   fraudtransactions_fraudtransaction_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fraudtransactions_fraudtransaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public.fraudtransactions_fraudtransaction_id_seq;
       public          postgres    false    222                       0    0 )   fraudtransactions_fraudtransaction_id_seq    SEQUENCE OWNED BY     w   ALTER SEQUENCE public.fraudtransactions_fraudtransaction_id_seq OWNED BY public.fraudtransactions.fraudtransaction_id;
          public          postgres    false    221            �            1259    24620    notifications    TABLE       CREATE TABLE public.notifications (
    notification_id integer NOT NULL,
    message text NOT NULL,
    type character varying(50) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    fraudtransaction_id integer,
    fraudaccount_id integer
);
 !   DROP TABLE public.notifications;
       public         heap    postgres    false            �            1259    24619 !   notifications_notification_id_seq    SEQUENCE     �   CREATE SEQUENCE public.notifications_notification_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.notifications_notification_id_seq;
       public          postgres    false    218                       0    0 !   notifications_notification_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.notifications_notification_id_seq OWNED BY public.notifications.notification_id;
          public          postgres    false    217            _           2604    24615    cases open_case_id    DEFAULT     x   ALTER TABLE ONLY public.cases ALTER COLUMN open_case_id SET DEFAULT nextval('public.cases_open_case_id_seq'::regclass);
 A   ALTER TABLE public.cases ALTER COLUMN open_case_id DROP DEFAULT;
       public          postgres    false    215    216    216            b           2604    24642    fraudaccounts fraudaccount_id    DEFAULT     �   ALTER TABLE ONLY public.fraudaccounts ALTER COLUMN fraudaccount_id SET DEFAULT nextval('public.fraudaccounts_fraudaccount_id_seq'::regclass);
 L   ALTER TABLE public.fraudaccounts ALTER COLUMN fraudaccount_id DROP DEFAULT;
       public          postgres    false    220    219    220            c           2604    24651 %   fraudtransactions fraudtransaction_id    DEFAULT     �   ALTER TABLE ONLY public.fraudtransactions ALTER COLUMN fraudtransaction_id SET DEFAULT nextval('public.fraudtransactions_fraudtransaction_id_seq'::regclass);
 T   ALTER TABLE public.fraudtransactions ALTER COLUMN fraudtransaction_id DROP DEFAULT;
       public          postgres    false    222    221    222            `           2604    24623    notifications notification_id    DEFAULT     �   ALTER TABLE ONLY public.notifications ALTER COLUMN notification_id SET DEFAULT nextval('public.notifications_notification_id_seq'::regclass);
 L   ALTER TABLE public.notifications ALTER COLUMN notification_id DROP DEFAULT;
       public          postgres    false    218    217    218                      0    24612    cases 
   TABLE DATA           [   COPY public.cases (open_case_id, status, fraudaccount_id, fraudtransaction_id) FROM stdin;
    public          postgres    false    216   �0                 0    24639    fraudaccounts 
   TABLE DATA           �   COPY public.fraudaccounts (fraudaccount_id, customer_id, first_name, last_name, account_balance, age, address, mobileno, addharno, lastlogin, branchid, account_type, emailid, upi_id, account_number, pancard_number, city) FROM stdin;
    public          postgres    false    220   �0                 0    24648    fraudtransactions 
   TABLE DATA           �   COPY public.fraudtransactions (fraudtransaction_id, transactionid, transactiontype, amount_before_transaction, amount_after_transaction, transaction_date, from_account_id, to_account_id) FROM stdin;
    public          postgres    false    222   1                 0    24620    notifications 
   TABLE DATA           y   COPY public.notifications (notification_id, message, type, created_at, fraudtransaction_id, fraudaccount_id) FROM stdin;
    public          postgres    false    218   *1                  0    0    cases_open_case_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.cases_open_case_id_seq', 1, false);
          public          postgres    false    215                       0    0 !   fraudaccounts_fraudaccount_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.fraudaccounts_fraudaccount_id_seq', 1, false);
          public          postgres    false    219                       0    0 )   fraudtransactions_fraudtransaction_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('public.fraudtransactions_fraudtransaction_id_seq', 1, false);
          public          postgres    false    221                       0    0 !   notifications_notification_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.notifications_notification_id_seq', 1, false);
          public          postgres    false    217            f           2606    24618    cases cases_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.cases
    ADD CONSTRAINT cases_pkey PRIMARY KEY (open_case_id);
 :   ALTER TABLE ONLY public.cases DROP CONSTRAINT cases_pkey;
       public            postgres    false    216            j           2606    24646     fraudaccounts fraudaccounts_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.fraudaccounts
    ADD CONSTRAINT fraudaccounts_pkey PRIMARY KEY (fraudaccount_id);
 J   ALTER TABLE ONLY public.fraudaccounts DROP CONSTRAINT fraudaccounts_pkey;
       public            postgres    false    220            l           2606    24653 (   fraudtransactions fraudtransactions_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public.fraudtransactions
    ADD CONSTRAINT fraudtransactions_pkey PRIMARY KEY (fraudtransaction_id);
 R   ALTER TABLE ONLY public.fraudtransactions DROP CONSTRAINT fraudtransactions_pkey;
       public            postgres    false    222            h           2606    24628     notifications notifications_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (notification_id);
 J   ALTER TABLE ONLY public.notifications DROP CONSTRAINT notifications_pkey;
       public            postgres    false    218            m           2606    24664     cases cases_fraudaccount_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cases
    ADD CONSTRAINT cases_fraudaccount_id_fkey FOREIGN KEY (fraudaccount_id) REFERENCES public.fraudaccounts(fraudaccount_id);
 J   ALTER TABLE ONLY public.cases DROP CONSTRAINT cases_fraudaccount_id_fkey;
       public          postgres    false    4714    220    216            n           2606    24669 $   cases cases_fraudtransaction_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cases
    ADD CONSTRAINT cases_fraudtransaction_id_fkey FOREIGN KEY (fraudtransaction_id) REFERENCES public.fraudtransactions(fraudtransaction_id);
 N   ALTER TABLE ONLY public.cases DROP CONSTRAINT cases_fraudtransaction_id_fkey;
       public          postgres    false    216    4716    222            o           2606    24659 0   notifications notifications_fraudaccount_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_fraudaccount_id_fkey FOREIGN KEY (fraudaccount_id) REFERENCES public.fraudaccounts(fraudaccount_id);
 Z   ALTER TABLE ONLY public.notifications DROP CONSTRAINT notifications_fraudaccount_id_fkey;
       public          postgres    false    220    218    4714            p           2606    24654 4   notifications notifications_fraudtransaction_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_fraudtransaction_id_fkey FOREIGN KEY (fraudtransaction_id) REFERENCES public.fraudtransactions(fraudtransaction_id);
 ^   ALTER TABLE ONLY public.notifications DROP CONSTRAINT notifications_fraudtransaction_id_fkey;
       public          postgres    false    218    222    4716                  x������ � �            x������ � �            x������ � �            x������ � �     
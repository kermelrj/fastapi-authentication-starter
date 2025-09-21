CREATE TABLE IF NOT EXISTS public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  hashed_password TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO public.users (email, full_name) VALUES
('alice@example.com', 'Alice Doe', 'hashedpassword1'),
('bob@example.com',   'Bob Roe', 'hashedpassword2')
ON CONFLICT DO NOTHING;

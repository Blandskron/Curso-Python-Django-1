ALTER TABLE productos
ADD CONSTRAINT chk_precio CHECK (precio > 0);
CREATE OR REPLACE FUNCTION org.fn_audit_orders()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO org.audit_log(table_name, action, record_id)
  VALUES ('orders', TG_OP, COALESCE(NEW.order_id, OLD.order_id));
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION public.faiu_renglonorden()
  RETURNS trigger AS
$BODY$
 DECLARE
	w_puntoventa integer;
	w_idstock integer;
	w_cantidad integer;
	w_tipodeorden integer;
	cantidadaux integer;
 BEGIN	
	IF (TG_OP = 'INSERT') THEN
		SELECT puntodeventa_id INTO w_puntoventa
        FROM inventario_orden WHERE id = NEW.orden_id;

		SELECT tipodeorden INTO w_tipodeorden
        FROM inventario_orden WHERE id = NEW.orden_id;

		SELECT cantidad INTO w_cantidad
        FROM inventario_stock WHERE puntodeventa_id = w_puntoventa AND libro_id = NEW.libro_id;  

		SELECT id INTO w_idstock
        FROM inventario_stock WHERE puntodeventa_id = w_puntoventa AND libro_id = NEW.libro_id; 
		
		IF (w_idstock IS NOT NULL) THEN -- ya existe el stock,lo actualizo
			cantidadaux = NEW.cantidad;
			IF (w_tipodeorden < 3) THEN -- orde de salida por ende descuento
				cantidadaux = cantidadaux * -1;				
			END IF;
			cantidadaux = w_cantidad + cantidadaux ;
			UPDATE inventario_stock SET cantidad = cantidadaux 
			WHERE puntodeventa_id = w_puntoventa AND libro_id = NEW.libro_id;
		ELSE
			INSERT INTO public.inventario_stock(cantidad, libro_id, puntodeventa_id)
    		VALUES (NEW.cantidad, NEW.libro_id, w_puntoventa);
		END IF;
	END IF;

	IF (TG_OP = 'UPDATE') THEN					
		RAISE EXCEPTION 'ERROR: No se puede actulizar el reglon de una orden. Debe crear una orden de entrada o salida para corregir';		
	END IF;
	
	IF (TG_OP = 'DELETE') THEN					
		RAISE EXCEPTION 'ERROR: No se puede borrar un reglon de una orden';		
	END IF;

	return NEW;
 END;
  $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

CREATE TRIGGER taiu_renglonorden
  AFTER INSERT OR UPDATE
  ON public.inventario_renglonorden
  FOR EACH ROW
  EXECUTE PROCEDURE public.faiu_renglonorden();

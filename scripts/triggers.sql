-- ----------------------------
-- Scheme Log
-- ----------------------------

DROP TABLE IF EXISTS "public"."cb_scheme_log";
CREATE TABLE "public"."cb_scheme_log" (
  "operation" varchar(1),
  "stamp" timestamp(6),
  "user_id" text,
  "id" int4,
  "scheme_name" varchar(50),
  "date_of_approval" date,
  "date_of_establishment" date,
  "relevant_authority" int4,
  "land_rights_office" int4,
  "region" int4,
  "title_deed_number" varchar(30),
  "registration_division" int4,
  "area" numeric(15,4),
  "doc_imposing_conditions_number" varchar(30),
  "constitution_ref_number" varchar(32),
  "no_of_plots" int4,
  "scheme_number" varchar(32),
  "sg_number" varchar (32),
  "plot_status" int4,
  "scheme_description" varchar(200)
)
;

-- ----------------------------
-- Holder Log
-- ----------------------------
DROP TABLE IF EXISTS "public"."cb_holder_log";
CREATE TABLE "public"."cb_holder_log" (
  "operation" varchar(1),
  "stamp" timestamp(6),
  "user_id" text,
  "id" int4,
  "plot_number" int4,
  "transfer_contract_date" date,
  "plot_use" int4,
  "holder_first_name" varchar(50),
  "holder_surname" varchar(50),
  "holder_gender" int4,
  "holder_identifier" varchar(20),
  "holder_date_of_birth" date,
  "marital_status" int4,
  "nature_of_marriage" int4,
  "holder_disability_status" int4,
  "holder_income_level" int4,
  "holder_occupation" int4,
  "spouse_surname" varchar(50),
  "spouse_first_name" varchar(50),
  "spouse_gender" int4,
  "spouse_identifier" varchar(20),
  "spouse_date_of_birth" date,
  "other_dependants" int4,
  "juristic_person_name" varchar(50),
  "juristic_person_number" varchar(50)
)
;

----  TRIGGER FUNCTIONS

-- CREATE OR REPLACE FUNCTION cb_scheme_log() RETURNS TRIGGER AS $cb_scheme_log$
--     BEGIN
--         --
--         -- Create a row in lht_approval_log to reflect the operation performed on cb_scheme,
--         -- make use of the special variable TG_OP to work out the operation.
--         --
--         IF (TG_OP = 'DELETE') THEN
--             INSERT INTO cb_scheme_log SELECT 'D', now(), user, OLD.*;
--             RETURN OLD;
--         ELSIF (TG_OP = 'UPDATE') THEN
--             INSERT INTO cb_scheme_log SELECT 'U', now(), user, NEW.*;
--             RETURN NEW;
--         ELSIF (TG_OP = 'INSERT') THEN
--             INSERT INTO cb_scheme_log SELECT 'I', now(), user, NEW.*;
--             RETURN NEW;
--         END IF;
--         RETURN NULL; -- result is ignored since this is an AFTER trigger
--     END;
-- $cb_scheme_log$ LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION cb_holder_log() RETURNS TRIGGER AS $cb_holder_log$
--     BEGIN
--         --
--         -- Create a row in lht_approval_log to reflect the operation performed on cb_holder,
--         -- make use of the special variable TG_OP to work out the operation.
--         --
--         IF (TG_OP = 'DELETE') THEN
--             INSERT INTO cb_holder_log SELECT 'D', now(), user, OLD.*;
--             RETURN OLD;
--         ELSIF (TG_OP = 'UPDATE') THEN
--             INSERT INTO cb_holder_log SELECT 'U', now(), user, NEW.*;
--             RETURN NEW;
--         ELSIF (TG_OP = 'INSERT') THEN
--             INSERT INTO cb_holder_log SELECT 'I', now(), user, NEW.*;
--             RETURN NEW;
--         END IF;
--         RETURN NULL; -- result is ignored since this is an AFTER trigger
--     END;
-- $cb_holder_log$ LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION insert_plots() RETURNS TRIGGER AS $insert_plots$
--     BEGIN
--         --- Update plot from lis_plot
--         INSERT INTO cb_plot (geom, upi, use)
-- 	    SELECT
-- 	    t.geom, t.upi, u."id"
-- 	    FROM
-- 	    cb_lis_plot t
-- 	    INNER JOIN cb_check_lht_plot_use u ON u."value" = t.use
-- 	    WHERE t.geom NOT IN (select geom from cb_plot);
--         RETURN NULL;
--     END;
--
-- $insert_plots$ LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION comment_user_timestamp() RETURNS TRIGGER AS $comment_user_timestamp$
--     BEGIN
--         NEW.user_id = (SELECT cb_user."id" FROM cb_user WHERE cb_user.user_name = "session_user"());
-- 		RETURN NEW;
--     END;
-- $comment_user_timestamp$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insert_timestamp() RETURNS TRIGGER AS $insert_timestamp$
    BEGIN
        NEW.timestamp = NOW();
				RETURN NEW;
    END;

$insert_timestamp$ LANGUAGE plpgsql;

--- TRIGGERS

-- CREATE TRIGGER cb_scheme_log
-- AFTER INSERT OR UPDATE OR DELETE ON cb_scheme
--     FOR EACH ROW EXECUTE PROCEDURE cb_scheme_log();
--
-- CREATE TRIGGER cb_holder_log
-- AFTER INSERT OR UPDATE OR DELETE ON cb_holder
--     FOR EACH ROW EXECUTE PROCEDURE cb_holder_log();

-- CREATE TRIGGER insert_plots
-- AFTER INSERT ON cb_lis_plot
--     FOR EACH ROW EXECUTE PROCEDURE insert_plots();

CREATE TRIGGER comment_timestamp
BEFORE INSERT OR UPDATE ON cb_comment
    FOR EACH ROW EXECUTE PROCEDURE insert_timestamp();

-- CREATE TRIGGER comment_user_timestamp
-- BEFORE INSERT OR UPDATE ON cb_comment
--     FOR EACH ROW EXECUTE PROCEDURE comment_user_timestamp();

CREATE TRIGGER insert_workflow_timestamp
BEFORE INSERT OR UPDATE ON cb_scheme_workflow
    FOR EACH ROW EXECUTE PROCEDURE insert_timestamp();

---- TODO Add exception handling

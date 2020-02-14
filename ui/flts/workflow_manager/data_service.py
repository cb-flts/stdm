"""
/***************************************************************************
Name                 : Data Service
Description          : Data service package that handles data provision for
                       workflow manager modules; Scheme Establishment and
                       First, Second and Third Examination FLTS modules.
Date                 : 22/August/2019
copyright            : (C) 2019
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from abc import ABCMeta, abstractmethod
from sqlalchemy import (
    exc,
    func
)
from sqlalchemy.orm import joinedload
from stdm.ui.flts.workflow_manager.config import (
    ColumnSettings,
    CommentConfig,
    DocumentConfig,
    FilterQueryBy,
    HolderConfig,
    PlotImportFileConfig,
    PlotImportPreviewConfig,
    PlotViewerConfig,
    BeaconViewerConfig,
    BeaconImportPreviewConfig,
    ServitudeViewerConfig,
    ServitudeImportPreviewConfig,
    SchemeConfig,
    TableModelIcons,
)
from stdm.data.configuration import entity_model


class DataService:
    """
    Data service abstract class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def columns(self):
        """
        Scheme columns options
        """
        raise NotImplementedError

    def collections(self):
        """
        Related entity name
        """
        raise NotImplementedError

    def related_entities(self, entity):
        """
        Related entity name identified by a foreign key
        :param entity: Profile entity
        :type entity: Entity
        :return: Related entity names
        :rtype: List
        """
        fk_entity_name = []
        for col in entity.columns.values():
            if col.TYPE_INFO == 'FOREIGN_KEY' or \
                    col.TYPE_INFO == 'LOOKUP':
                fk_entity_name.append(col.parent.name)
        return fk_entity_name

    def run_query(self):
        """
        Run query on an entity
        :return:
        """
        raise NotImplementedError

    def entity_model_(self, entity):
        """
        Gets entity model
        :param entity: Profile entity
        :type entity: Entity
        :return model: Entity model
        :rtype model: DeclarativeMeta
        """
        try:
            model = entity_model(entity)
            return model
        except AttributeError as e:
            raise e

# TODO: Refactor repeating methods in all these classes


class SchemeDataService(DataService):
    """
    Scheme data model service
    """
    def __init__(self, current_profile, widget_obj_name, parent):
        self._profile = current_profile
        self.entity_name = "Scheme"
        self._parent = parent
        self._widget_obj_name = widget_obj_name
        self._scheme_config = SchemeConfig(self._parent)
        self._table_model_icons = TableModelIcons()

    @property
    def columns(self):
        """
        Scheme table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self._scheme_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return False

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons

    @property
    def lookups(self):
        """
        Scheme table view lookup options
        :return: Lookup options
        :rtype: LookUp
        """
        return self._scheme_config.lookups

    @property
    def save_columns(self):
        """
        Scheme table view save column options
        :return: Save column options
        :rtype: List
        """
        return self._scheme_config.scheme_save_columns

    @property
    def update_columns(self):
        """
        Scheme table view update column options
        :return: Update column options
        :rtype: List
        """
        return self._scheme_config.scheme_update_columns

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return self._scheme_config.collections

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else self.entity_name
            entity = self._profile.entity(entity_name)
            return super(SchemeDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        workflow_id = self.get_workflow_id(self._widget_obj_name)
        scheme_workflow_model = self.entity_model_("Scheme_workflow")
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                options(joinedload(model.cb_check_lht_land_rights_office)). \
                options(joinedload(model.cb_check_lht_region)). \
                options(joinedload(model.cb_check_lht_relevant_authority)). \
                filter(
                    scheme_workflow_model.scheme_id == model.id,
                    scheme_workflow_model.workflow_id == workflow_id
                )
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def get_workflow_id(self, attr):
        """
        Return workflow id/primary key
        :param attr: Workflow lookup attribute
        :return workflow_id: Workflow id/primary key
        :rtype workflow_id: Integer
        """
        workflow_id = getattr(self.lookups, attr, None)
        if workflow_id:
            workflow_id = workflow_id()
        return workflow_id

    def filter_in(self, entity_name, filters):
        """
        Return query objects as a collection of filter using in_ operator
        :param entity_name: Name of entity to be queried
        :type entity_name: String
        :param filters: Query filter columns and values
        :type filters: Dictionary
        :return: Query object results
        :rtype: Query
        """
        model = self.entity_model_(entity_name)
        entity_object = model()
        filters = [
            getattr(model, key).in_(value) for key, value in filters.iteritems()
        ]
        return entity_object.queryObject().filter(*filters)

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(SchemeDataService, self).entity_model_(entity)

    @staticmethod
    def filter_query_by(entity_name, filters):
        """
        Filters query result by a column value
        :param entity_name: Entity name
        :type entity_name: String
        :param filters: Column filters - column name and value
        :type filters: Dictionary
        :return: Filter entity query object
        :rtype: Entity object
        """
        try:
            filter_by = FilterQueryBy()
            return filter_by(entity_name, filters)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def workflow_ids(self):
        """
        Returns workflow IDs
        :return workflow_ids: Workflow record ID
        :rtype workflow_ids: List
        """
        workflow_ids = [
            self.lookups.schemeLodgement(),
            self.lookups.schemeEstablishment(),
            self.lookups.firstExamination(),
            self.lookups.secondExamination(),
            self.lookups.thirdExamination()
        ]
        return workflow_ids


class DocumentDataService(DataService):
    """
    Scheme supporting documents data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "supporting_document"
        self._document_config = DocumentConfig()
        self._table_model_icons = TableModelIcons()

    @property
    def columns(self):
        """
        Scheme supporting documents
        table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self._document_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons

    @property
    def lookups(self):
        """
        Scheme supporting documents lookup options
        :return: Lookup options
        :rtype: LookUp
        """
        return self._document_config.lookups

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return self._document_config.collections

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else self.entity_name
            entity = self._profile.entity(entity_name)
            return super(DocumentDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model, sp_doc_model = self.entity_model_(self.entity_name)
        scheme_model, sc_doc_model = self.entity_model_("Scheme")
        entity_object = model()
        try:
            query_object = entity_object.queryObject().filter(
                sc_doc_model.supporting_doc_id == model.id,
                sc_doc_model.scheme_id == self._scheme_id
            ).order_by(model.last_modified)
            return query_object.all()
        except (exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity and supporting document model
        :param name: Name of the entity
        :type name: String
        :return model: Entity model
        :rtype model: DeclarativeMeta
        :return document_model: Supporting document entity model
        :rtype document_model: DeclarativeMeta
        """
        try:
            entity = self._profile.entity(name)
            model, document_model = entity_model(
                entity, with_supporting_document=True
            )
            return model, document_model
        except AttributeError as e:
            raise e


class HolderDataService(DataService):
    """
    Scheme holders data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "Scheme"
        self._holder_config = HolderConfig()

    @property
    def columns(self):
        """
        Scheme holder table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self._holder_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def load_collections(self):
        """
        Related entity collection names to be used as
        primary table view load
        :return: Related entity collection names
        :rtype: List
        """
        return self._holder_config.load_collections

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return self._holder_config.collections

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else "Holder"
            entity = self._profile.entity(entity_name)
            return super(HolderDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                filter(model.id == self._scheme_id)
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(HolderDataService, self).entity_model_(entity)


class CommentDataService(DataService):
    """
    Comment Manager data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "Scheme"
        self._comment_config = CommentConfig()

    @property
    def columns(self):
        """
        Comment Manager widget columns options
        :return: Comment Manager widget columns and query columns options
        :rtype: List
        """
        return self._comment_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return False

    @property
    def lookups(self):
        """
        Comment text edit lookup options
        :return: Lookup options
        :rtype: LookUp
        """
        return self._comment_config.lookups

    @property
    def save_columns(self):
        """
        Comment text edit save column options
        :return: Save column values
        :rtype: List
        """
        return self._comment_config.comment_save_columns

    @property
    def load_collections(self):
        """
        Related entity collection names to be used as
        primary load data for the Comment Manager widget
        :return: Related entity collection names
        :rtype: List
        """
        return self._comment_config.load_collections

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return self._comment_config.collections

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else "Comment"
            entity = self._profile.entity(entity_name)
            return super(CommentDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                filter(model.id == self._scheme_id)
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(CommentDataService, self).entity_model_(entity)


class PlotViewerDataService(DataService):
    """
    Scheme plot viewer data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "Plot"
        self.plot_viewer_config = PlotViewerConfig()

    @property
    def columns(self):
        """
        Scheme plot viewer table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self.plot_viewer_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else self.entity_name
            entity = self._profile.entity(entity_name)
            return super(PlotViewerDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                filter(model.scheme_id == self._scheme_id)
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(PlotViewerDataService, self).entity_model_(entity)


class BeaconViewerDataService(DataService):
    """
    Scheme beacon viewer data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "Beacon"
        self.beacon_viewer_config = BeaconViewerConfig()

    @property
    def columns(self):
        """
        Scheme beacon viewer table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self.beacon_viewer_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else self.entity_name
            entity = self._profile.entity(entity_name)
            return super(BeaconViewerDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                filter(model.scheme_id == self._scheme_id)
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(BeaconViewerDataService, self).entity_model_(entity)


class ServitudeViewerDataService(DataService):
    """
    Scheme servitude viewer data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self.entity_name = "Servitude"
        self.servitude_viewer_config = ServitudeViewerConfig()

    @property
    def columns(self):
        """
        Scheme servitude viewer table view columns options
        :return: Table view columns and query columns options
        :rtype: List
        """
        return self.servitude_viewer_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers
                 or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        :return: Related entity names
        :rtype: List
        """
        try:
            entity_name = entity_name if entity_name else self.entity_name
            entity = self._profile.entity(entity_name)
            return super(ServitudeViewerDataService, self).related_entities(entity)
        except AttributeError as e:
            raise e

    def run_query(self):
        """
        Run query on an entity
        :return query_obj: Query results
        :rtype query_obj: List
        """
        model = self.entity_model_(self.entity_name)
        entity_object = model()
        try:
            query_object = entity_object.queryObject(). \
                filter(model.scheme_id == self._scheme_id)
            return query_object.all()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(ServitudeViewerDataService, self).entity_model_(entity)


def plot_viewer_data_service(import_type):
    """
    Returns plot viewier data service
    based on import type
    :param import_type: Plot file import type
    :type import_type: String
    :return: Plot viewer data service object
    :rtype: Service Object
    """
    data_service = {
        "Plots": PlotViewerDataService,
        "Servitudes": ServitudeViewerDataService,
        "Beacons": BeaconViewerDataService
    }
    return data_service[import_type]


class PlotImportFileDataService:
    """
    Scheme plot import file data model service
    """
    def __init__(self):
        self._plot_config = PlotImportFileConfig()
        self._table_model_icons = TableModelIcons()

    @property
    def columns(self):
        """
        Scheme plot import file
        table view columns options
        :return: Table view columns
        :rtype: List
        """
        return self._plot_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers or False otherwise
        :rtype: Boolean
        """
        return False

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons


class PlotPreviewDataService(DataService):
    """
    Scheme plot import preview data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._scheme_id = scheme_id
        self._plot_config = PlotImportPreviewConfig()
        self._table_model_icons = TableModelIcons()
        self._scheme = self._get_scheme()

    @property
    def columns(self):
        """
        Scheme plot import preview
        table view columns options
        :return: Table view columns
        :rtype: List
        """
        return self._plot_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons

    @property
    def save_columns(self):
        """
        Plot import save column options
        :return: Save column values
        :rtype: List
        """
        return self._plot_config.plot_save_columns

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        """
        pass

    def run_query(self):
        """
        Run query on an entity
        """
        pass

    def _get_scheme(self):
        """
        Returns Scheme record/row
        :return: Scheme record/row
        :rtype: Entity
        """
        return self.filter_query_by("Scheme", {"id": self._scheme_id}).first()

    def scheme_plot_numbers(self):
        """
        Returns Scheme plot numbers
        :return plot_numbers: Scheme Relevant Authority record/row
        :rtype plot_numbers: Entity
        """
        filters = {"scheme_id": self._scheme_id}
        model = self.entity_model_("Plot")
        plot_numbers = self.filter_query_by(
            "Plot",
            filters,
            [getattr(model, "plot_number")]
        ).distinct()
        return plot_numbers

    def scheme_relevant_authority(self):
        """
        Returns Scheme Relevant Authority record/row
        :return relevant_authority: Scheme Relevant Authority record/row
        :rtype relevant_authority: Entity
        """
        filters = {
            "type_of_relevant_authority": self._scheme.relevant_authority,
            "region": self._scheme.region
        }
        model = self.entity_model_("Relevant_authority")
        relevant_authority = self.filter_query_by(
            "Relevant_authority",
            filters,
            [getattr(model, "au_code")]
        ).first()
        return relevant_authority

    @staticmethod
    def filter_query_by(entity_name, filters, columns=None):
        """
        Filters query result by a column value
        :param entity_name: Entity name
        :type entity_name: String
        :param filters: Column filters - column name and value
        :type filters: Dictionary
        :type columns: Fields to select from
        :type columns: List
        :return: Filter entity query object
        :rtype: Entity object
        """
        try:
            filter_by = FilterQueryBy()
            return filter_by(entity_name, filters, columns)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(PlotPreviewDataService, self).entity_model_(entity)


class ServitudePreviewDataService(DataService):
    """
    Scheme servitude import preview data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._servitude_config = ServitudeImportPreviewConfig()
        self._table_model_icons = TableModelIcons()

    @property
    def columns(self):
        """
        Scheme servitude import preview
        table view columns options
        :return: Table view columns
        :rtype: List
        """
        return self._servitude_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons

    @property
    def save_columns(self):
        """
        Servitude import save column options
        :return: Save column values
        :rtype: List
        """
        return self._servitude_config.servitude_save_columns

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        """
        pass

    def run_query(self):
        """
        Run query on an entity
        """
        pass

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(ServitudePreviewDataService, self).entity_model_(entity)


class BeaconPreviewDataService(DataService):
    """
    Scheme beacon import preview data model service
    """
    def __init__(self, current_profile, scheme_id):
        self._profile = current_profile
        self._beacon_config = BeaconImportPreviewConfig()
        self._table_model_icons = TableModelIcons()

    @property
    def columns(self):
        """
        Scheme beacon import preview
        table view columns options
        :return: Table view columns
        :rtype: List
        """
        return self._beacon_config.columns

    @property
    def vertical_header(self):
        """
        Scheme table view vertical orientation
        :return: True for vertical headers or False otherwise
        :rtype: Boolean
        """
        return True

    @property
    def icons(self):
        """
        QAbstractTableModel icon options
        :return: QAbstractTableModel icon options
        :rtype: Dictionary
        """
        return self._table_model_icons.icons

    @property
    def save_columns(self):
        """
        Beacon import save column options
        :return: Save column values
        :rtype: List
        """
        return self._beacon_config.beacon_save_columns

    @property
    def collections(self):
        """
        Related entity collection names
        :return: Related entity collection names
        :rtype: List
        """
        return False

    def related_entities(self, entity_name=None):
        """
        Related entity name identified by foreign keys
        :param entity_name:
        :type entity_name: String
        """
        pass

    def run_query(self):
        """
        Run query on an entity
        """
        pass

    def entity_model_(self, name=None):
        """
        Gets entity model
        :param name: Name of the entity
        :type name: String
        :return: Entity model
        :rtype: DeclarativeMeta
        """
        entity = self._profile.entity(name)
        return super(BeaconPreviewDataService, self).entity_model_(entity)


def plot_data_service(import_type):
    """
    Returns plot preview data service
    based on import type
    :param import_type: Plot file import type
    :type import_type: String
    :return: Plot preview data service object
    :rtype: Service Object
    """
    data_service = {
        "Plots": PlotPreviewDataService,
        "Servitudes": ServitudePreviewDataService,
        "Beacons": BeaconPreviewDataService
    }
    return data_service[import_type]

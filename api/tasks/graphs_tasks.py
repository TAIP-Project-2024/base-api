from celery import shared_task

from api.services.general.graph_drawing_service import GraphDrawingService


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def build_new_graphs(self):
        GraphDrawingService().process_topic(topic='politics', clear_all=True)
        print('BA Hello from cron task!')
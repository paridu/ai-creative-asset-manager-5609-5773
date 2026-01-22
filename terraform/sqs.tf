resource "aws_sqs_queue" "ingestion_queue" {
  name                        = "asset-ingestion-queue.fifo"
  fifo_queue                  = true
  content_based_deduplication = true
  visibility_timeout_seconds  = 300 # 5 mins for AI processing
}

resource "aws_sqs_queue" "ingestion_dlq" {
  name = "asset-ingestion-dlq"
}

resource "aws_sqs_queue_redrive_policy" "ingestion_policy" {
  queue_url = aws_sqs_queue.ingestion_queue.id
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.ingestion_dlq.arn
    maxReceiveCount     = 3
  })
}
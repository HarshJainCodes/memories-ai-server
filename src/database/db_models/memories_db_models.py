from __future__ import annotations

import enum
from uuid import UUID

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
	pass


class MessageType(enum.IntEnum):
	Root = 0
	Text = 1
	Think = 2
	System = 3


class RoleType(enum.IntEnum):
	User = 0
	Assistant = 1
	System = 2
	Tool = 3


class VerificationCodes(Base):
	__tablename__ = "VerificationCodes"

	user_email: Mapped[str] = mapped_column("UserEmail", String(450), primary_key=True)
	otp: Mapped[int] = mapped_column("OTP", Integer, nullable=False)

	issued_at: Mapped[DateTime] = mapped_column(
		"IssuedAt", DateTime(timezone=True), nullable=False
	)


class UserInfo(Base):
	__tablename__ = "UserInfo"

	name: Mapped[str] = mapped_column("Name", String(), nullable=False)
	email: Mapped[str] = mapped_column("Email", String(450), nullable=False, index=True)
	user_id: Mapped[str] = mapped_column(
		"UserId", Integer, nullable=False, primary_key=True
	)
	is_manual_login: Mapped[bool] = mapped_column(
		"IsManualLogin", Boolean, nullable=False, default=False
	)
	password: Mapped[str] = mapped_column(
		"Password", String, nullable=False, default=""
	)
	profile_pic_url: Mapped[str] = mapped_column(
		"ProfilePictureURL", nullable=False, default=""
	)

	chat_conversations: Mapped[list[ChatbotConversations]] = relationship(
		back_populates="user_info"
	)


class ChatbotConversations(Base):
	__tablename__ = "ChatbotConversations"

	conversation_id: Mapped[UUID] = mapped_column(
		"ConversationId", Uuid, primary_key=True, nullable=False
	)
	user_email: Mapped[str] = mapped_column("UserEmail", ForeignKey("UserInfo.Email"))
	conversation_name: Mapped[str] = mapped_column(
		"ConversationName", String, nullable=False
	)
	created_at: Mapped[DateTime] = mapped_column("CreatedAt", DateTime, nullable=False)

	conversation_messages: Mapped[list[ChatMessages]] = relationship(
		back_populates="chat_conversation"
	)

	user_info: Mapped[UserInfo] = relationship(back_populates="chat_conversations")


class ChatMessages(Base):
	__tablename__ = "ChatMessages"

	message_id: Mapped[UUID] = mapped_column("MessageId", Uuid, primary_key=True)
	conversation_id: Mapped[UUID] = mapped_column(
		ForeignKey("ChatbotConversations.ConversationId", ondelete="CASCADE")
	)
	reasoning_content: Mapped[str] = mapped_column(
		"ReasoningContent", String, nullable=True
	)
	type: Mapped[MessageType] = mapped_column("Type", Integer, nullable=False)
	timestamp: Mapped[DateTime] = mapped_column("Timestamp", DateTime, nullable=False)
	content: Mapped[str] = mapped_column("Content", String, nullable=False, default="")
	model: Mapped[str] = mapped_column("Model", String, nullable=True, default="")
	role: Mapped[RoleType] = mapped_column(
		"Role", Integer, nullable=False, default=RoleType.User
	)
	tool_call_id: Mapped[str] = mapped_column("ToolCallId", String, nullable=True)
	tool_calls: Mapped[str] = mapped_column("ToolCalls", String, nullable=True)

	chat_conversation: Mapped[ChatbotConversations] = relationship(
		back_populates="conversation_messages"
	)

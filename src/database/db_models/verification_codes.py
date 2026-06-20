from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	pass


class VerificationCodes(Base):
	__tablename__ = "VerificationCodes"

	user_email: Mapped[str] = mapped_column("UserEmail", String(450), primary_key=True)
	otp: Mapped[int] = mapped_column("OTP", Integer, nullable=False)

	issued_at: Mapped[DateTime] = mapped_column(
		"IssuedAt", DateTime(timezone=True), nullable=False
	)

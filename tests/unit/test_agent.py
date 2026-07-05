"""Documentation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_api_docs():
    """Test Generate OpenAPI/Swagger documentation from source code."""
    tools = AgentTools()
    result = await tools.generate_api_docs(source_dir="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_architecture_diagram():
    """Test Generate architecture diagram from codebase analysis."""
    tools = AgentTools()
    result = await tools.generate_architecture_diagram(project_root="test", diagram_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_changelog():
    """Test Generate changelog from git commit history."""
    tools = AgentTools()
    result = await tools.generate_changelog(from_ref="test", to_ref="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_stale_docs():
    """Test Find documentation that is out of sync with code."""
    tools = AgentTools()
    result = await tools.detect_stale_docs(docs_dir="test", source_dir="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.documentation_agent_agent import DocumentationAgentAgent
    agent = DocumentationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
